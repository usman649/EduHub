from django.db import models
from abstaction.created import BaseModel
from blog.models import User
from ckeditor.fields import RichTextField

class Course(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="course")
    title = models.CharField(max_length=300)
    is_finished = models.BooleanField(default=False)



class Lesson(BaseModel):
    course = models.ForeignKey("Course", on_delete=models.CASCADE,related_name="lesson")
    title = models.CharField(max_length=300)
    video = models.FileField(upload_to="course/video", null=True, blank=True)
    content = RichTextField(blank=True,null=True)


class Test(BaseModel):
    lesson = models.ForeignKey("Lesson", on_delete=models.CASCADE,related_name="test")
    title = models.CharField(max_length=300)


    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

class Follow(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="subscribe_user")
    course = models.ForeignKey("Course", on_delete=models.CASCADE,related_name="subscribe_course")


class TestBasicModel(BaseModel):
    test = models.ForeignKey("Test", on_delete=models.CASCADE,related_name="test_basic_test")
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="test_basic_user")

    result = models.BooleanField(default=True)
    started_at = models.DateTimeField(auto_now_add=True)