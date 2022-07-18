from django.db import models
from django.forms import ModelForm

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    email = models.EmailField(max_length=50)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    status_book =[
        ('Available','Available'),
        ('Borrowed','Borrowed')
    ]
    status = models.CharField(max_length=50,choices=status_book, null=True,blank=True)
    category = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    publishedYear = models.DateField()
    author = models.CharField(max_length=50)
    active = models.BooleanField(default=True)
   
    user = models.ForeignKey(Client, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Borrow(models.Model):
    title = models.CharField(max_length=50)
    time = models.IntegerField()
    user = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

