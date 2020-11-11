from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    def __str__(self):
        return self.category_name


class Master(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    categorys = models.ManyToManyField(Category)
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Object(models.Model):
    X = models.CharField(max_length=10)
    Y = models.CharField(max_length=10)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(default=timezone.now)
    categorys = models.ManyToManyField(Category)
    def __str__(self):
        return 'Объект №{}'.format(self.id)


class Gallery(models.Model):
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    photo =  models.ImageField()
