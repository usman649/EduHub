from blog.serialazer import UserSerializer
from course.models import Course, Lesson, Test, Follow,TestBasicModel
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = ("id","lesson","title")


class LessonSerializer(ModelSerializer):
    test = TestSerializer(many=True,read_only=True)
    class Meta:
        model = Lesson
        fields = ("id","course","title","video","content","test")


class CourseSerializer(ModelSerializer):
    lesson = LessonSerializer(many=True,read_only=True)
    user = serializers.CharField(source="user.username",read_only=True)

    class Meta:
        model = Course
        fields = ("id","title","user","lesson")








class FollowSerializer(ModelSerializer):
    user = serializers.CharField(source="user.username",read_only=True)
    course = serializers.CharField(source="course.title",read_only=True)
    class Meta:
        model = Follow
        fields = ("id","user","course")

class TestBasicSerializer(ModelSerializer):
    class Meta:
        model = TestBasicModel
        fields = ("id","user","test","result")