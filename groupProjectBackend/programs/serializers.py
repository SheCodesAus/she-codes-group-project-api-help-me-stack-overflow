from rest_framework import serializers
from .models import Programs

#Programs Serialzer
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

#Programs Detail Serialzer to allow for editing/put function in views
class ProgramsDetailSerializer(ProgramsSerializer):

    def update(self, instance, validated_data):
        instance.date_created = validated_data.get('date_created',instance.date_created)
        instance.modefied_at = validated_data.get('modefied_at',instance.modefied_at)
        instance.title = validated_data.get('title',instance.title)
        instance.description = validated_data.get('description',instance.description)
        instance.image = validated_data.get('image',instance.image)
        instance.date_start = validated_data.get('date_start',instance.date_start)
        instance.date_end = validated_data.get('date_end',instance.date_end)
        instance.location = validated_data.get('location',instance.location)
        instance.coding_languages = validated_data.get('coding_languages',instance.coding_languages)
        instance.student_attendees = validated_data.get('student_attendees',instance.student_attendees) 
        instance.mentors = validated_data.get('mentors',instance.mentors)
        instance.save()
        return instance