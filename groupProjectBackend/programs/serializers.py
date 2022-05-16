from rest_framework import serializers
from .models import Programs

class ProgramsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.DateTimeField(read_only=True)
    modefied_at = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None)
    image = serializers.URLField()
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    location = serializers.CharField(max_length=200)
    coding_languages = serializers.CharField(max_length=200)
    student_attendees = serializers.CharField(max_length=200) 
    mentors = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Programs.objects.create(**validated_data)