from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type']

admin.site.register(CustomUser,UserModel)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Staff_Leave)
admin.site.register(Staff_Feedback)
admin.site.register(Student_Feedback)
admin.site.register(Forgot_password)
admin.site.register(Attendance)
admin.site.register(Attendance_Report)
admin.site.register(Student_Result)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','photo','timing','designation']
admin.site.register(Team,TeamAdmin)

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name','photo','profession','feedback']
admin.site.register(Testimonial,TestimonialAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','subject','message']
admin.site.register(Contact,ContactAdmin)

class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name','number','email','firstSubject','secondSubject','message']
admin.site.register(Inquiry,InquiryAdmin)

class PopularCoursesAdmin(admin.ModelAdmin):
    list_display = ['courseName','photo','timing','price','instructorName','time','studentsNumber']
admin.site.register(PopularCourses,PopularCoursesAdmin)