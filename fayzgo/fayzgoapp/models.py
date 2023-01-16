from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True)


class About(models.Model):
    about_uz = models.TextField(max_length=1500, null=True, blank=True)
    about_ru = models.TextField(max_length=1500, null=True, blank=True)
    about_en = models.TextField(max_length=1500, null=True, blank=True)


class Service(models.Model):
    name_uz = models.CharField(max_length=50, null=True, blank=True)
    name_ru = models.CharField(max_length=50, null=True, blank=True)
    name_en = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True)
    description_uz = models.TextField(max_length=1500, null=True, blank=True)
    description_ru = models.TextField(max_length=1500, null=True, blank=True)
    description_en = models.TextField(max_length=1500, null=True, blank=True)


class Client(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(null=True)
