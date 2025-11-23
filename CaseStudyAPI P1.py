from django.db import models

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name
