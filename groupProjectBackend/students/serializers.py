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


class StudentsDetailSerializer(StudentsSerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.contact_email = validated_data.get('contact_email',instance.contact_email)
        instance.contact_phone = validated_data.get('contact_phone',instance.contact_phone)
        instance.biography = validated_data.get('biography',instance.biography)
        instance.location = validated_data.get('location',instance.location)
        instance.demographic_gender = validated_data.get('demographic_gender',instance.demographic_gender)
        instance.demographic_nationality = validated_data.get('demographic_nationality',instance.demographic_nationality)
        instance.social_linkedin = validated_data.get('social_linkedin',instance.social_linkedin)
        instance.social_github = validated_data.get('social_github',instance.social_github)
        instance.employment_company = validated_data.get('emplayment_company',instance.employment_company)
        instance.employment_position = validated_data.get('employment_position',instance.employment_position)
        instance.employment_industry = validated_data.get('employment_industry',instance.employment_industry)
        instance.employment_salary = validated_data.get('employment_salary',instance.employment_salary)
        instance.program_attendence = validated_data.get('program_attendence',instance.program_attendence)
        instance.coding_languages = validated_data.get('coding_languages',instance.coding_languages)
        instance.save()
        return instance
