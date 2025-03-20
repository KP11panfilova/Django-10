from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=50, choices=[
        ('художественная литература', 'Художественная литература'),
        ('нон-фикшн', 'Нон-фикшн'),
        ('научная фантастика', 'Научная фантастика'),
    ])

    def __str__(self):
        return self.get_name_display()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    published_date = models.DateField()
    genre = models.CharField(max_length=50, choices=[
        ('художественная литература', 'Художественная литература'),
        ('нон-фикшн', 'Нон-фикшн'),
        ('научная фантастика', 'Научная фантастика'),
    ])
    is_checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def is_available(self):
        return not self.is_checked_out

class Tag(models.Model):
    name = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)

    def __str__(self):
        return self.slug

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    text = models.TextField(blank=True, null=True)
    image = models.URLField()
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='posts/')
    createdAt = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title