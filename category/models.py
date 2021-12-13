from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField()
    cart_image = models.ImageField(upload_to='images/')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    
    def get_url(self):
        return reverse('product_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name
        