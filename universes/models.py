from django.db import models

class Universe(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name