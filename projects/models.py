from django.db import models

from category.models import *


# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    details = models.TextField()
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    target = models.IntegerField()
    is_cancelled = models.BooleanField(default=False)
    # relationships
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
