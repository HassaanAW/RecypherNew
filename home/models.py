from django.db import models
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

# Create your models here.
class Registerations(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    password = models.CharField(max_length=122)

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=122)
    code = models.CharField(max_length=122)
    points = models.IntegerField(default=0)
    total_members = models.IntegerField(default=0)
    P1 = models.CharField(max_length=122, blank=True)
    P2 = models.CharField(max_length=122, blank=True)
    P3 = models.CharField(max_length=122, blank=True)
    P4 = models.CharField(max_length=122, blank=True)
    
    def __str__(self):
        return self.name

class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

# Create your models here.
class User_Emails(models.Model):
    Team_Code = models.CharField(max_length=122, default=0)
    From = models.CharField(max_length=122)
    To = models.CharField(max_length=122)
    Subject = models.CharField(max_length=122)
    Body = RichTextField(blank=True, null=True)
    Date = models.DateTimeField()

    def __str__(self):
        return self.From + " -> " + self.To

class Scores(models.Model):
    code = models.CharField(max_length=122)
    name = models.CharField(max_length=122)
    points = models.IntegerField(default=0)
    q1 = models.CharField(max_length=122, blank=True)
    q2 = models.CharField(max_length=122, blank=True)
    q3 = models.CharField(max_length=122, blank=True)
    q4 = models.CharField(max_length=122, blank=True)
    q5 = models.CharField(max_length=122, blank=True)
    q6 = models.CharField(max_length=122, blank=True)
    q7 = models.CharField(max_length=122, blank=True)
    q8 = models.CharField(max_length=122, blank=True)
    q9 = models.CharField(max_length=122, blank=True)
    q10 = models.CharField(max_length=122, blank=True)

    def __str__(self):
        return self.name