from django.db import models
class URL(models.Model):
    long_url =models.URRLField()
    short_url=models.charField(max_length=20,unique=True)