from django.db import models


class Post(models.Model):
    #title
    #image
    #text
    #date
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    text=models.TextField(max_length=300, null=True)
    date=models.DateField()
    image=models.ImageField(upload_to="")