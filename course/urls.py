from django.urls import path
from course.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('course', CourseCreate)
router.register("lesson",LessonCreate)
router.register("test",TestCreate)


urlpatterns = [
    path('follow/', follow_student_view),
    path("teacher/", teacher_ability_view),
    path("student/", student_ability_view),
    path("statistic/<int:course_id>/", statistic_view),
    path("exam/<int:test_id>/", exam_view),
    path("test/basic/",test_basic_view),

]

urlpatterns += router.urls