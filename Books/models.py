from django.db import models

# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    pages=models.IntegerField()
    price=models.IntegerField(default=100)


    def __str__(self):
        return self.book_name



