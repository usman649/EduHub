from django.contrib import admin
from course.models import *





class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_finished')
    list_display_links = ('id', 'title', 'user', 'is_finished')
    search_fields = ('title', 'user__username')
    list_filter = ('is_finished',"created_at")



class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'course')
    list_display_links = ('id', 'title', 'course')
    search_fields = ('title', 'course__title')
    list_filter = ('course',"created_at")



class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'lesson__title', 'start_date', 'end_date')
    list_display_links = ('id', 'title', 'lesson__title', 'start_date', 'end_date')
    search_fields = ('title', 'lesson__title')
    list_filter = ('start_date', 'end_date')



class FollowAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course')
    list_display_links = ('id', 'user', 'course')
    search_fields = ('user__username', 'course__title')
    list_filter = ('course',"created_at")



class TestBasicModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username', 'test', 'result')
    list_display_links = ('id', 'user__username', 'test', 'result')
    search_fields = ('user__username', 'test__title')
    list_filter = ('result', 'started_at')















admin.site.register(Course,CourseAdmin)
admin.site.register(Lesson,LessonAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Follow,FollowAdmin)
admin.site.register(TestBasicModel,TestBasicModelAdmin)
