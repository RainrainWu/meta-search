from django.db import models

# Create your models here.

class History(models.Model):

    keyword = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
