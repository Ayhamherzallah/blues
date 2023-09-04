from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    subCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class product(models.Model):
    category = models.ManyToManyField(Category, related_name='category')
    subCategory = models.ManyToManyField(SubCategory, related_name='sub')
    menuitem = models.ManyToManyField(MenuItems,blank=True)
    name = models.CharField(max_length=55)
    benefits = RichTextField(null=True, blank=True)
    ideal_for = RichTextField(null=True, blank=True)
    image = CloudinaryField('image')

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=55, blank=True, null=True)
    Flavor = models.CharField(max_length=55, blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return str(self.product.name)



