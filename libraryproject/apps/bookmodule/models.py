from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name="address")

    class Student2(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Address2(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    students = models.ManyToManyField(Student2, related_name='addresses')

class ImageModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')

