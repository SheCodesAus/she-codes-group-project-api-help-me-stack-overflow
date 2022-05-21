from rest_framework import serializers
from .models import Reports

class ReportsSerlializer(serializers.Serializer):
    location = serializers.CharField(max_length=200)
    demographic_gender = serializers.CharField(max_length=200)
    demographic_nationality = serializers.CharField(max_length=200)
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

        






