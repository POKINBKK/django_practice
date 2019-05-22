from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    topic = models.CharField(null=False, max_length=150)
    story = models.TextField(null=False)
    date = models.DateField()
    like = models.IntegerField()
    GENRE = (
        ('0', 'Horror'),
        ('1', 'Romantic'),
        ('2', 'SCI-FI')
    )
    genre = models.CharField(max_length=1, choices=GENRE)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.CharField(max_length=75)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
