from django.db import models

# Create your models here.

class History(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=512, default="")
    result = models.CharField(max_length=4096, default="")
