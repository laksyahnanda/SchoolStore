from django.contrib import admin
from django.contrib.auth.models import User
from .models import Department, Course, Order, User


# Register your models here.
class DepartmentAdmin(admin.ModelAdmin):
    list_display=['name','wikipedia_link']
    prepopulated_fields = {'wikipedia_link':('name',)}
admin.site.register(Department,DepartmentAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=['name','department']
    prepopulated_fields = {'name':('name',)}
admin.site.register(Course,CourseAdmin)


admin.site.register(User)
admin.site.register(Order)