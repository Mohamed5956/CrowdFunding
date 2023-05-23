from django.db import models

from projects.models import *


# Create your models here.
class Images(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.CharField(max_length=70)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
