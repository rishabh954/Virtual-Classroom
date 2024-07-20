from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from ssa_app.emailbackend import EmailBackEnd
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from ssa_app.models import CustomUser
from django.core.mail import send_mail
from django.contrib import messages
import uuid
from ssa import settings
from ssa_app.utils import *
from .models import *

def home(request):
    testimonialData = Testimonial.objects.all()
    teamData = Team.objects.all()
    popularCourses = PopularCourses.objects.all()
    data = {
        'testimonialData':testimonialData,
        'teamData':teamData,
        'popularCourses':popularCourses,
    }
    return render(request,"index.html",data)

def team(request):
    testimonialData = Testimonial.objects.all()
    teamData = Team.objects.all()
    popularCourses = PopularCourses.objects.all()
    data = {
        'testimonialData':testimonialData,
        'teamData':teamData,
        'popularCourses':popularCourses,
    }
    return render(request,"team.html",data)

def contact(request):
    if request.method == "POST":
        NAME = request.POST.get("name")
        EMAIL = request.POST.get("email")
        SUBJECT = request.POST.get("subject")
        MESSAGE = request.POST.get("message")
        CONTACTFORM = Contact(name=NAME,email=EMAIL,subject=SUBJECT,message=MESSAGE)
        CONTACTFORM.save()
    return render(request,"contact.html")

def courses(request):
    testimonialData = Testimonial.objects.all()
    popularCourses = PopularCourses.objects.all()
    data = {
        'testimonialData':testimonialData,
        'popularCourses':popularCourses,
    }
    return render(request,"courses.html",data)

def about(request):
    teamData = Team.objects.all()
    data = {
        'teamData':teamData,
    }
    return render(request,"about.html",data)

def error(request):
    return render(request,"error.html")

def testimonial(request):
    testimonialData = Testimonial.objects.all()
    teamData = Team.objects.all()
    popularCourses = PopularCourses.objects.all()
    data = {
        'testimonialData':testimonialData,
        'teamData':teamData,
        'popularCourses':popularCourses,
    }
    return render(request,"testimonial.html",data)

def homelogin(request):
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        NAME = request.POST.get("name")
        NUMBER = request.POST.get("number")
        EMAIL = request.POST.get("email")
        FIRSTSUBJECT = request.POST.get("firstSubject")
        SECONDSUBJECT = request.POST.get("secondSubject")
        MESSAGE = request.POST.get("message")
        INQUIRYFORM = Inquiry(name=NAME,number=NUMBER,email=EMAIL,firstSubject=FIRSTSUBJECT,secondSubject=SECONDSUBJECT,message=MESSAGE)
        INQUIRYFORM.save()
    return render(request, "subject.html")

def dologin(request):
    if request.method == 'POST':
        user = EmailBackEnd.authenticate(request
                                        ,username=request.POST.get('email'),
                                        password=request.POST.get('password'),)
        
        if user != None:
            login(request,user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('profile')
            elif user_type == '2':
                return redirect('profile')
            elif user_type == '3':
                return redirect('profile')
            else:
                messages.error(request,'wrong email and password')
                redirect('login')
        else:
                messages.error(request,'wrong email and password')
                redirect('login')
    return render(request,'login.html')
    

def dologout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def hod_home(request):
    return render(request,'hod/home.html')



@login_required(login_url='login')
def profile(request):
    user = CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user
    }
    return render(request,'profile.html',context)



@login_required(login_url='login')
def profile_update(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        
        try:
            customuser = CustomUser.objects.get(id = request.user.id)
            customuser.first_name = first_name
            customuser.last_name = last_name

            if password != None and password != "":
                customuser.set_password(password)

            if profile_pic != None and profile_pic != "":
                customuser.profile_pic = profile_pic
                
            customuser.save()
            messages.success(request,"profile update sucessfully")
            return redirect('profile')
        except:
            messages.error(request,"failed to update your profile")
            return redirect('profile')

    return redirect('profile')
    

# def change_password(request,token):
#     context = {}
#     try:
#         profile_obj = Forgot_password.objects.get(forgot_password_token = token)
#         print(profile_obj)

#     except Exception as e:
#         print(e)
#     return render(request,'change_password.html')

# def forgot_password(request):
#     try:
#         if request.method == 'POST':
#             femail = request.POST.get('email')

#             if CustomUser.objects.filter(email = femail).exists():
#                 user_obj = CustomUser.objects.get(email = femail)
#                 token = str(uuid.uuid4())
#                 # send_forgot_password_mail(user_obj,token)
#                 messages.error(request,'email send successfully')
#                 return redirect('forgot_password')
       
#             else:
#                 messages.error(request,'email not exist')
#                 return redirect('forgot_password')
#     except:
#         pass
#     return render(request,'forgotpassword.html')