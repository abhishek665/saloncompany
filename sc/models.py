from django.db import models
import os

# Create your models here.


def get_image_path(instance, filename):
    # define the path where the image should be uploaded
    return os.path.join('uploads', 'services', filename)


class Services(models.Model):

    uid = models.IntegerField(default=0)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name


def get_sub_image_path(instance, filename):
    # define the path where the image should be uploaded
    return os.path.join('uploads', 'services', instance.name, filename)


class SubCategory(models.Model):

    uid = models.IntegerField(default=0)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to=get_sub_image_path, blank=True, null=True)

    def __str__(self):
        return self.name


class AtomCategory(models.Model):
    FACE_CHOICES = (
        ('Dry Skin', 'Dry Skin'),
        ('Oily Skin', 'Oily Skin'),
        ('All Types', 'All Types')
    )

    BRAND_CHOICES = (
        ('Loreal', 'Loreal'),
        ('Pearls', 'Pearls'),
        ('Nivia', 'Nivia')
    )

    uid = models.IntegerField(default=0)
    atom = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(default=0)
    benefits = models.CharField(max_length=255, blank=True, null=True)
    face_type = models.CharField(max_length=255, blank=True, null=True, choices=FACE_CHOICES)
    discount = models.CharField(max_length=255, blank=True, null=True)
    brand_products = models.CharField(max_length=255, blank=True, null=True, choices=BRAND_CHOICES)


class Order(models.Model):

    email = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    order = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email