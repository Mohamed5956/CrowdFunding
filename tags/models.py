from django.db import models
from projects.models import *


# Create your models here.
class Tags(models.Model):
    id = models.AutoField(primary_key=True)
    tag = models.CharField(max_length=70)
    # relationships
    projects = models.ManyToManyField(Project)


