from django.db import models

# Create your models here.
from django.db import models
from  datetime import time,date


class Category(models.Model):
    title = models.CharField(max_length=100)


class Student(models.Model):
    student_id = models.IntegerField()
    s_firstname = models.CharField(max_length=100)
    s_lastname = models.CharField(max_length=100)
    s_year = models.CharField(max_length=100)
    s_section = models.CharField(max_length=100)


class Book(models.Model):
    title = models.CharField(max_length=100)

    category = models.ManyToManyField(Category,related_name='book_category')
    cover = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.IntegerField(default=0)



class Borrow(models.Model):
    book=models.ManyToManyField(Book)
    student=models.ManyToManyField(Student)
    qty=models.PositiveIntegerField(default=0)
    date=models.DateField(default=date.today)
    status=models.CharField(max_length=30)

    def book_list(self):
        return ', '.join([a.title for a in self.book.all()])
    def student_list(self):
        return ','.join([s.s_firstname for s in self.student.all()])



