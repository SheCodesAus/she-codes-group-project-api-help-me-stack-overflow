from rest_framework import serializers
from .models import Students

class StudentsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    contact_email = serializers.CharField(max_length=200)
    contact_phone = serializers.CharField(max_length=200)
    biography = serializers.CharField(max_length=None)
    location = serializers.CharField(max_length=200)
    demographic_gender = serializers.CharField(max_length=200)
    demographic_nationality = serializers.CharField(max_length=200)
    social_linkedin = serializers.URLField()
    social_github = serializers.URLField()
    employment_company = serializers.CharField(max_length=200)
    employment_position = serializers.CharField(max_length=200)
    employment_industry = serializers.CharField(max_length=200)
    employment_salary = serializers.IntegerField()
    program_attendence = serializers.CharField(max_length=200)
    coding_languages = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Students.objects.create(**validated_data)