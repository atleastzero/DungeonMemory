from django.db import models
import uuid

UNIVERSE_GENRE = (
    ("sf", "space"), 
    ("fa", "fantasy"),
    ("pa", "post-apocalyptic")
)

class Universe(models.Model):
    name                = models.CharField(max_length=50)
    genre               = models.CharField(max_length=20, choices=UNIVERSE_GENRE, default='fa')
    universe_id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_updated        = models.DateTimeField(auto_now=True)
    created             = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name                = models.CharField(max_length=50)
    size                = models.CharField(max_length=200)
    total_population    = models.IntegerField()
    last_visited        = models.DateTimeField(auto_now=True)
    place_id            = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class PlaceDemographics(models.Model):
    place               = models.ForeignKey(Place, on_delete=models.CASCADE)
  # race                = models.ForeignKey(Character, on_delete=models.CASCADE)
    population          = models.IntegerField()