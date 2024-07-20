from django.shortcuts import render,redirect
from ssa.settings import EMAIL_HOST_USER
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import random

def AddStudent(request):
    course = Course.objects.all()
    session = Session.objects.all()

    if request.method == 'POST':
        s_first_name = request.POST.get('s_first_name')
        s_last_name = request.POST.get('s_last_name')
        s_email = request.POST.get('s_email')
        s_password = request.POST.get('s_password')
        # s_password = " "
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
        address = request.POST.get('s_address')
        s_username = request.POST.get('s_username')

        

        if CustomUser.objects.filter(email = s_email).exists():
            messages.warning(request,"email is already taken")
            return redirect('AddStudent')
        
        elif CustomUser.objects.filter(username = s_username).exists():
            messages.warning(request,"username is already taken")
            return redirect('AddStudent')
        

        else:
            user = CustomUser(
                first_name=s_first_name,    
                last_name=s_last_name,
                email=s_email,
                password = s_password,
                username = s_username,
                user_type = 3,
            )
            user.set_password(s_password)
            user.save()
            course = Course.objects.get(id=course_id)
            session = Session.objects.get(id=session_id)

            student = Student(
                admin = user,
                address = address,
                course_id= course,
                session_id= session,
                gender = gender,
            )
            student.save()
            messages.success(request," Student " + user.first_name + " added succesfully !")
            return redirect('ViewStudent')


    context = {
        "course":course,
        "session":session,
    }

        
    return render(request,"hod/AddStudent.html",context)

@login_required(login_url='login')
def ViewStudent(request):
    student = Student.objects.all()
    context = {
        "student":student,
        
    }
    return render(request,'hod/ViewStudent.html',context)

def EditStudent(request,id):
    student = Student.objects.filter(id=id)
    course = Course.objects.all()
    session = Session.objects.all()

    context = {
        "student":student,
        "course":course,
        "session":session,
    }
    return render(request,'hod/EditStudent.html',context)

def UpdateStudent(request):
    if request.method == 'POST':

        stu_id = request.POST.get('stu_id')
        s_first_name = request.POST.get('s_first_name')
        s_last_name = request.POST.get('s_last_name')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_id = request.POST.get('session_id')
        address = request.POST.get('s_address')
        s_username = request.POST.get('s_username')
        s_email = request.POST.get('s_email')
        
        user = CustomUser.objects.get(id = stu_id)
        user.first_name = s_first_name
        user.last_name = s_last_name
        user.email = s_email
        user.username = s_username

        user.save()
        student = Student.objects.get(admin = stu_id)
        student.address = address
        student.gender = gender

        course = Course.objects.get(id = course_id)
        student.course_id = course

        session = Session.objects.get(id = session_id)
        student.session_id = session

        student.save()
        messages.success(request,user.first_name + ' are successfully updated')
        return redirect('ViewStudent')

    return render(request,'hod/EditStudent.html')


def DeleteStudent(request,admin):
        student = CustomUser.objects.get(id = admin)
        student.delete()
        messages.success(request,student.first_name + ' are successfully deleted')
        return redirect('ViewStudent')

    
def AddCourse(request):
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        short_course_name = request.POST.get('short_course_name')

        course = Course(
            name = course_name,
            short_name = short_course_name,
        )
        course.save()
        messages.success(request,course.name + ' are added successfully')
        return redirect('ViewCourse')

    return render(request,'hod/AddCourse.html')



def ViewCourse(request):
    course = Course.objects.all()
    context = {
        "course":course,
    }
    return render(request,'hod/ViewCourse.html',context)


def EditCourse(request,id):
    course = Course.objects.get(id = id)
    context = {
         "course":course,
    }
    return render(request,'hod/EditCourse.html',context)

def UpdateCourse(request):
    if request.method == 'POST':
        addcourse = request.POST.get('course')
        short_name = request.POST.get('short_name')
        c_id = request.POST.get('id')

        course = Course.objects.get(id=c_id)
        course.name = addcourse
        course.short_name = short_name
        course.save()
        messages.success(request,course.name + ' in short ' + course.short_name + '')
        return redirect('ViewCourse')

    return render(request,'hod/EditCourse.html')

def DeleteCourse(request,id):
      try:  
        course = Course.objects.get(id=id)
        course.delete()
        messages.success(request,course.short_name + ' are successfully deleted')
        return redirect('ViewCourse')
      except:
        messages.success(request,'YOU MUST HAVE TO BE ONE COURSE')
        return redirect('ViewCourse')
          


def AddStaff(request):
    if request.method == 'POST':
        
        profile_pic = request.FILES.get('profile_pic')
        s_first_name = request.POST.get('s_first_name')
        s_last_name = request.POST.get('s_last_name')
        s_email = request.POST.get('s_email')
        s_password = request.POST.get('s_password')
        # s_password = " "
        gender = request.POST.get('gender')
        address = request.POST.get('s_address')
        s_username = request.POST.get('s_username')

        if CustomUser.objects.filter(email = s_email).exists():
            messages.warning(request,"email is already taken")
            return redirect('AddStaff')
        
        elif CustomUser.objects.filter(username = s_username).exists():
            messages.warning(request,"username is already taken")
            return redirect('AddStaff')
        
        else:
            user = CustomUser(
                first_name=s_first_name,    
                last_name=s_last_name,
                email=s_email,
                password = s_password,
                username = s_username,
                profile_pic = profile_pic,
                user_type = 2,
                )
            user.set_password(s_password)
            user.save()

            staff = Staff(
                admin = user,
                gender = gender,
                address = address,
            )   
            staff.save()


            messages.success(request," Staff " + user.first_name + " added succesfully !")
            return redirect('ViewStaff')

    return render(request,'hod/AddStaff.html')

def ViewStaff(request):
    staff = Staff.objects.all()
    context = {
        "staff":staff
    }
    return render(request,'hod/ViewStaff.html',context)

def EditStaff(request,id):
    staff = Staff.objects.get(id=id)
    context = {
        "staff":staff,
    }
    return render(request,'hod/EditStaff.html',context)

def UpdateStaff(request):
    if request.method == 'POST':

        staff_id = request.POST.get('staff_id')
        profile_pic = request.FILES.get('profile_pic')
        s_first_name = request.POST.get('s_first_name')
        s_last_name = request.POST.get('s_last_name')
        gender = request.POST.get('gender')
        address = request.POST.get('s_address')
        s_username = request.POST.get('s_username')
        s_email = request.POST.get('s_email')
        
        

        user = CustomUser.objects.get(id = staff_id)
        user.first_name = s_first_name
        user.last_name = s_last_name
        user.email = s_email
        user.username = s_username

        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic

        user.save()
        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender
        staff.save()
        messages.success(request," Staff " + user.first_name + " edited succesfully !")
        return redirect('ViewStaff')
    return render(request,'hod/EditStaff.html')


def DeleteStaff(request,admin):
        staff = CustomUser.objects.get(id = admin)
        staff.delete()
        messages.success(request,staff.first_name +' are successfully deleted')
        return redirect('ViewStaff')
      
def AddSubject(request,):
    course = Course.objects.all()
    staff = Staff.objects.all()

    if request.method == 'POST':
        sub_name = request.POST.get('sub_name')
        sub_short_name = request.POST.get('sub_short_name')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')

        course_i = Course.objects.get(id=course_id)
        staff_i = Staff.objects.get(id=staff_id)

        subject = Subject(
            name = sub_name,
            short_name = sub_short_name,
            course = course_i,
            staff = staff_i,
        )

        subject.save()
        messages.success(request,"subject " + subject.name + " added succesfully !")
        return redirect('ViewSubject')

    context = {
        "course":course,
        "staff":staff,
    }
    return render(request,'hod/AddSubject.html',context)

def ViewSubject(request):
    subjects = Subject.objects.all()
    course = Course.objects.all()

    context = {
        "subjects":subjects,
        "course":course,
    }
    return render(request,'hod/ViewSubject.html',context)

def EditSubject(request,id):
    subject = Subject.objects.get(id=id)
    course = Course.objects.all()
    staff = Staff.objects.all()
    context = {
        "subject":subject,
        "course":course,
        "staff":staff,
    }
    return render(request,'hod/EditSubject.html',context)

def UpdateSubject(request):
    if  request.method == 'POST':
        subject_id = request.POST.get('id')
        course_id = request.POST.get('course_id')
        staff_id = request.POST.get('staff_id')
        name = request.POST.get('name')
        short_name = request.POST.get('short_name')

        course = Course.objects.get(id=course_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            id = subject_id,
            name = name,
            short_name = short_name,
            course = course,
            staff = staff,
        )
        subject.save()
        messages.success(request,"Data Updated Successfully")
        return redirect('ViewSubject')

    return render(request,'hod/EditSubject.html',)

def DeleteSubject(request,id):
    subject = Subject.objects.get(id=id)
    subject.delete()
    messages.warning(request,subject.short_name+" deleted successfully!")
    return redirect('ViewSubject')

def AddSession(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        session = Session(
            session_start = start_date,
            session_end = end_date)
        session.save()
        messages.success(request,"Added Successfully")
        return redirect('AddSession')

    return render(request,'hod/AddSession.html')

def ViewSession(request):
    sessions = Session.objects.all()
    context = {
        "sessions":sessions
    }
    return render(request,'hod/ViewSession.html',context)

def EditSession(request,id):
    session = Session.objects.filter(id=id)
    context = {
        "session":session,
    }
    return render(request,'hod/EditSession.html',context)

def UpdateSession(request):
    if request.method == 'POST':
        s_id = request.POST.get('id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        session = Session(
            id=s_id,
            session_start = start_date,
            session_end = end_date)
        session.save()
        messages.success(request,"Session updated successfully")
        return redirect('ViewSession')
    

def DeleteSession(request,id):
    try:
        session = Session.objects.get(id=id)
        session.delete()
        messages.error(request,"Deleted Successfully")
        return redirect('ViewSession')
    except:
        messages.error(request,"you can not delete this session")
        return redirect('ViewSession')



def StaffSendNotification(request,id):
    staff = Staff.objects.get(id=id)
    context = {
        "staff":staff
    }
    return render(request,'hod/StaffSendNotification.html',context)



def Save_staff(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        short_notification = request.POST.get('short_notification')
        message = request.POST.get('message')

        staff = Staff.objects.get(id=s_id)

        send_mail(
            'Your new task is ' + short_notification, message,EMAIL_HOST_USER,[staff.admin.email],fail_silently=False,
        )
        notification  = Staff_Notification(
            staff_id=staff,
            short_notification=short_notification,
            message=message
        )
        notification.save()
        messages.success(request,"Notification send successfully.")
        return redirect('ViewStaff')

    return render(request,'hod/StaffSendNotification.html')

def Staff_status(request):

    staff = Staff.objects.all()
    notification = Staff_Notification.objects.all().order_by('-id')[0:5]
    context = {

            "notifications" : notification,
            "staffs" : staff,
        }                      
    return render(request,'hod/Staff_status.html',context)


def StudentSendnotification(request,id):
    student = Student.objects.get(id=id)
    context = {
        "student":student
    }
    return render(request,'hod/StudentSendNotification.html',context)



def Save_student(request):
    if request.method == 'POST':
        s_id = request.POST.get('s_id')
        short_notification = request.POST.get('short_notification')
        message = request.POST.get('message')
        student = Student.objects.get(id=s_id)
        notification  = Student_Notification(
            student_id=student,
            short_notification=short_notification,
            message=message
        )
        notification.save()
        messages.success(request,"Notification send successfully.")
        return redirect('ViewStudent')

    return render(request,'hod/StaffSendNotification.html')

def Student_status(request):
    student = Student.objects.all()
    notification = Student_Notification.objects.all().order_by('-id')[0:5]
    context = {

            "notifications" : notification,
            "student" : student,
        }                      
    return render(request,'hod/Student_status.html',context)


def Staff_leave_view(request):
    staff_leave = Staff_Leave.objects.all()
    context = {
        "staff_leave": staff_leave
    }
    return render(request,'hod/Staff_leave_view.html',context)

def Staff_leave_approve(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('Staff_leave_view')
    

def Staff_leave_disapprove(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('Staff_leave_view')

def Student_leave_view(request):
    student_leave = Student_leave.objects.all()
    context = {
        "student_leave": student_leave,
    }
    return render(request,'hod/Student_leave_view.html',context)

def Student_leave_approve(request,id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('Student_leave_view')
    

def Student_leave_disapprove(request,id):
    leave = Student_leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('Student_leave_view')
    

def Student_view_attendance(request):

    subject = Subject.objects.all()
    session = Session.objects.all()
    
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    attendance_date = None
    attendance_report =None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session.objects.get(id = session_id)
            attendance = Attendance.objects.filter(subject_id = get_subject, attendance_date = attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_date = attendance_id)

    context = {
        'subject' : subject,
        'session' : session,
        'action' : action,
        'get_subject' : get_subject,
        'get_session' : get_session,
        'attendance_date' : attendance_date,
        'attendance_report' : attendance_report
    }
    return render(request,'hod/ViewAttendance.html',context)
