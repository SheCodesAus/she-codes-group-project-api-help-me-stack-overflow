from django.contrib.auth import get_user_model
from django.db import models

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    modefied_at = models.DateTimeField(auto_now_add=True)


class Programs(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    location = models.CharField(max_length=200)
    coding_languages = models.CharField(max_length=200)
    student_attendees = models.CharField(max_length=200) 
    mentors = models.CharField(max_length=200)
