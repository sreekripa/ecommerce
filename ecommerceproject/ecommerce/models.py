from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='Category'
        verbose_name_plural = 'Categories'
    def get_url(self):
        return reverse("ecommerce:Products_by_Category",args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(default=True)
    image=models.ImageField(upload_to='product',blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=('name',)
        verbose_name='Product'
        verbose_name_plural='Products'
    def get_url(self):
        return reverse("ecommerce:prodcatdetail",args=[self.category.slug,self.slug])


    def __str__(self):
        return '{}'.format(self.name)

