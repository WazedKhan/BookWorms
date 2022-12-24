from django.db import models

from autoslug import AutoSlugField


class Category(models.Model):
    """Category Model"""
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    """Book Model"""
    title = models.CharField(max_length=255)
    excerpt = models.TextField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Books"