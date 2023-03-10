from django.db import models

# Create your models here.
class Notes(models.Model):
    STATUS = (
        ("new", "NEWEST"),
        ("old", "OLDEST"),
        ("title", "TITLE"),
    )
    heading = models.CharField(max_length=100 )
    text = models.TextField(max_length=500)
    time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS, default="old")
    def __str__(self):
        return self.heading