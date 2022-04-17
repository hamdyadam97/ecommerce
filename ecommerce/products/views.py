from django.shortcuts import render,Http404
from .models import Product, ProductImage
# Create your views here.
def home(request):
    products = Product.objects.all()
    template = 'products/home.html'
    context = {'products':products}
    return render(request,template,context)

def all(request):
    products = Product.objects.all()
    context = {'products':products}
    template = 'products/all.html'
    return render(request,template,context)

def single(request,slug):
    try:
        product = Product.objects.get(slug=slug)
        images = ProductImage.objects.filter(product=product)
        context = {'product':product,'images':images}
        template = 'products/single.html'
        return render(request,template,context)
    except:
        raise Http404
def search(request):
    try:
        search = request.GET.get('search')
    except:
        search = None
    if search:
        product = Product.objects.filter(slug=search)
        context ={"query":search,'products':product}
        template = 'products/result.html'
    else:
        template = 'products/home.html'
        context = {}
    return render(request,template,context)