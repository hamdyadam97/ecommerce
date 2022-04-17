from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=100,decimal_places=2,default=29.9)
    sale_price = models.DecimalField(max_digits=100,decimal_places=2,default=29.9,null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False,auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
    class Meta:
        unique_together = ('title','slug')

    def get_price(self):
        return self.price

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('single',kwargs={'slug':self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/images/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.product.title


    def __str__(self):
        return self.product.title

class VARIATIONMANAGER(models.Manager,):
    def all(self):
        return super(VARIATIONMANAGER, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES = (
    ('size','size'),
    ('color','color'),
    ('package','package'),
)
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    category = models.CharField(max_length=120,choices=VAR_CATEGORIES,default='size')
    image = models.ForeignKey(ProductImage, null=True,blank=True ,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100,decimal_places=2,null=True,blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    object = VARIATIONMANAGER()

    def __unicode__(self):
        return self.title
    def __str__(self):
        return self.title
