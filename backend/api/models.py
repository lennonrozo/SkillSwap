from django.db import models
from django.contrib.models import User

class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    points = models.IntegerField(default=0)
    availability = models.CharField(max_length=100)
    certificates = models.TextField(blank=True)
    equipment_ready = models.BooleanField(default=False)
class Request(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_needed = models.ForeignKey(Skill, on_delete=models.CASCADE)
    time_requested = models.DateTimeField()
class Offer(models.Model):
    contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    proposed_time = models.DateTimeField()
    accepted = models.BooleanField(default=False)
class Review(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    contractor = models.ForeignKey(User, on_delete=models.CASCADE)
    problem_solved = models.BooleanField()
    photo = models.ImageField(upload_to='reviews/', blank=True, null=True)
    effectiveness_rating = models.IntegerField()
    personality_rating = models.IntegerField()
class PointSystem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points_earned = models.IntegerField(default=0)
    points_spent = models.IntegerField(default=0)