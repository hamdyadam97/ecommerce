# Generated by Django 3.0.7 on 2020-07-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20200722_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='notee',
            field=models.TextField(blank=True, null=True),
        ),
    ]