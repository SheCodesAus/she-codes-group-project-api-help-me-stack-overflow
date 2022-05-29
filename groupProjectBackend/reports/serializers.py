from rest_framework import serializers
from .models import Reports

class ReportsSerlializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    location = serializers.CharField(max_length=200)
    demographic_gender = serializers.CharField(max_length=200)
    demographic_nationality = serializers.CharField(max_length=200)
    program_name = serializers.CharField(max_length=100)
    total_attendance = serializers.IntegerField()
    program_attendence = serializers.IntegerField()
    attendee_to_alumni = serializers.IntegerField()
    alumni_to_mentor = serializers.IntegerField()
    program_date = serializers.DateTimeField()
    coding_languages = serializers.CharField(max_length=200)
    transition_to_tech = serializers.IntegerField()
    transition_to_other_program = serializers.IntegerField()
    transition_to_other_study = serializers.IntegerField()

    def create(self, validated_data):
        return Reports.objects.create(**validated_data)
        
    def update(self, instance, validated_data):
        instance.location = validated_data.get('location;', instance.location)
        instance.demographic_gender = validated_data.get('demographic_gender;', instance.demographic_gender)
        instance.demographic_nationality = validated_data.get('demographic_nationality;', instance.demographic_nationality)
        instance.program_name = validated_data.get('program_name;', instance.program_name)
        instance.total_attendance = validated_data.get('total_attendance;', instance.total_attendance)
        instance.program_attendence = validated_data.get('program_attendence;', instance.program_attendence)
        instance.attendee_to_alumni = validated_data.get('attendee_to_alumni;', instance.attendee_to_alumni)
        instance.alumni_to_mentor = validated_data.get('alumni_to_mentor;', instance.alumni_to_mentor)
        instance.program_date = validated_data.get('program_date;', instance.program_date)
        instance.coding_languages = validated_data.get('coding_languages;', instance.coding_languages)
        instance.transition_to_tech = validated_data.get('transition_to_tech;', instance.transition_to_tech)
        instance.transition_to_other_program = validated_data.get('transition_to_other_program;', instance.transition_to_other_program)
        instance.transition_to_other_study = validated_data.get('transition_to_other_study;', instance.transition_to_other_study)
        instance.save()
        return instance







