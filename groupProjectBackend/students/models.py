from django.db import models

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    modefied_at = models.DateTimeField(auto_now_add=True)

class Students(BaseModel):
    name = models.CharField(max_length=200)
    contact_email = models.CharField(max_length=200)
    contact_phone = models.CharField(max_length=200)
    biography = models.TextField()
    location = models.CharField(max_length=200)
    demographic_gender = models.CharField(max_length=200)
    demographic_nationality = models.CharField(max_length=200)
    social_linkedin = models.URLField()
    social_github = models.URLField()
    employment_company = models.CharField(max_length=200)
    employment_position = models.CharField(max_length=200)
    employment_industry = models.CharField(max_length=200)
    employment_salary = models.IntegerField()
    program_attendence = models.CharField(max_length=200)
    coding_languages = models.CharField(max_length=200)
