from django.db import models
from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='news')
    short_descriptions = models.TextField()
    long_descriptions = models.TextField(null=True)
    category = models.ForeignKey(CategoryModel,
                                 on_delete=models.PROTECT,
                                 related_name='news')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

