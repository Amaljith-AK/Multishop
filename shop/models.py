from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.


class ItemCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='pictures')
    stock = models.IntegerField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('prod_cat',args=[self.slug])

    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    img = models.ImageField(upload_to='product')
    price = models.IntegerField()
    offerprice = models.IntegerField()
    details = models.TextField(max_length=500,default='update please')
    category = models.ForeignKey(ItemCategory,on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    stock = models.IntegerField(default=1)

    def get_url(request):
        return reverse('details', args=[request.category.slug, request.slug])


    def __str__(self):
        return self.name

