from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_lenght=200)
    body =models.TextField()
    linked = models.ManyToManyField(User, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now-True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)