from django.db import models

class BaseModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    modefied_at = models.DateTimeField(auto_now_add=True)

class StudentCodingLanguages(BaseModel):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

class Students(BaseModel):
    class StudentStatus(models.TextChoices):
        Student = "Student"
        Alumni = "Alumni"
        Mentor = "Mentor"

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
    program_attendence = models.ManyToManyField(
        'programs.Programs',
        related_name="student_program_attendance"
    )
    coding_languages = models.ManyToManyField(
        'StudentCodingLanguages',
        related_name='coding_languages'
    )
    student_status = models.CharField(
        max_length=10,
        choices=StudentStatus.choices,
        null=True
    )



