from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class about(models.Model):
    name = models.CharField(max_length=20)
    dob = models.DateTimeField()
    college =models.CharField(max_length=30)
    cgpa = models.IntegerField(default=0)
    about= models.TextField(max_length=50)
    profile = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
 
    def __str__(self):
        return self.name