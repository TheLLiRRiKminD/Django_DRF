from rest_framework import serializers
from lms.models import Course, Lesson
from lms.vaidators import URLValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [URLValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(source='lesson_set.all', many=True)
    lessons_count = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'
