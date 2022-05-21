from rest_framework import serializers
from .models import StudentCodingLanguages, Students

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
    program_attendence = serializers.ReadOnlyField(source='program.id')
    coding_languages = serializers.SlugRelatedField(
        many=True,
        slug_field="slug",
        queryset=StudentCodingLanguages.objects.all()
    )
    student_status= serializers.CharField(max_length=10)

    def create(self, validated_data):
        # Get the list of Coding Languages out of validated data
        coding_languages = validated_data.pop('coding_languages')
        # create the Student record without the related Coding Languages
        student = Students.objects.create(**validated_data)
        # Add the Coding Languages using set. See https://docs.djangoproject.com/en/4.0/ref/models/relations/#django.db.models.fields.related.RelatedManager.set
        student.coding_languages.set(coding_languages)
        return student


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
        instance.student_status = validated_data.get('student_status',instance.student_status)
        instance.save()
        return instance

class StudentCodingLanguagesSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    category_name = serializers.CharField(max_length=50)
    slug = serializers.SlugField() 

    def create(self, validated_data):
        return StudentCodingLanguages.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.category_name = validated_data.get('category_name',instance.category_name)
        instance.slug = validated_data.get('slug',instance.slug)
        instance.save()
        return 

