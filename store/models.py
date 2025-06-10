from django.db import models
from django.utils import timezone

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

# Abstract base model for timestamps
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Book model inheriting from TimeStampedModel
class Book(TimeStampedModel):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ✅ FK for inline
    price = models.DecimalField(max_digits=6, decimal_places=2)
    published = models.BooleanField(default=False)
    published_date = models.DateField(null=True, blank=True)  # ✅ Used in admin

    def __str__(self):
        return self.title

# Manager for Proxy model
class PublishedBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

# Proxy model to filter published books
class PublishedBook(Book):
    objects = PublishedBookManager()

    class Meta:
        proxy = True
        ordering = ['-created_at']

    def mark_featured(self):
        return f"{self.title} is featured!"

# Multi-table inheritance for EBook
class EBook(Book):
    file_format = models.CharField(max_length=20)
    download_url = models.URLField()

    def __str__(self):
        return f"{self.title} (E-Book)"
