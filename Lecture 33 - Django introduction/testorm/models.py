from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        db_table = 'author'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'category'


class Book(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', default=1)
    category = models.ManyToManyField(Category)

    class Meta:
        db_table = 'book'



