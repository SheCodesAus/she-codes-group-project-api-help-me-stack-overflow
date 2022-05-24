from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Reports(models.Model):
    location = models.CharField(max_length=200)
    demographic_gender = models.CharField(max_length=200)
    demographic_nationality = models.CharField(max_length=200)
    program_name = models.CharField(null=True, max_length=100)
    total_attendance = models.IntegerField()
    program_attendence = models.IntegerField()
    attendee_to_alumni = models.IntegerField()
    alumni_to_mentor = models.IntegerField()
    program_date = models.DateTimeField()
    coding_languages = models.CharField(max_length=200)
    transition_to_tech = models.IntegerField()
    transition_to_other_program = models.IntegerField()
    transition_to_other_study = models.IntegerField()


