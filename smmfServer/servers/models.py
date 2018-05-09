from django.db import models

# Create your models here.
#
class User(models.Model):
    id_wx = models.CharField(max_length=64)
    photourl = models.CharField(max_length=256)
    name = models.CharField(max_length=64,null=True, blank=True)
    craete_time = models.DateTimeField(auto_now_add=True)
    recently_time = models.DateTimeField(auto_now=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name


class Ranking(models.Model):
    user = models.ForeignKey(User)
    photourl = models.CharField(max_length=256)
    name = models.CharField(max_length=64)
    rangking = models.IntegerField(null=True, blank=True)
    grade = models.IntegerField(default=0)
    craete_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.name