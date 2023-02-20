from django.db import models

# Create your models here.
class place(models.Model):
    title = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.title

class person(models.Model):
    pc = models.ImageField(upload_to='ppic')
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name