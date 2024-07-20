from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def Notification(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        Notification = Student_Notification.objects.filter(student_id=student_id)
        context = {
            "Notification":Notification,
        }
    return render(request,'student/notification.html',context)

def student_mark_as_done(request,status):
    notification = Student_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('studentNotification')
    
def STUDENT_LEAVE(request):
    return render(request,"student/apply_leave.html")

def STUDENT_LEAVE_SAVE(request):
    if request.method == 'POST':
        student_leave_date = request.POST.get('leave_date')
        leave_purpose = request.POST.get('leave_purpose')

        student = Student.objects.get(admin = request.user.id)
 
        leave = Student_leave(
            student_id = student,
            data = student_leave_date,
            message = leave_purpose,
        )
        leave.save()
        messages.success(request,'Leave successfully send')
    return render(request,"student/apply_leave.html")

def STUDENT_LEAVE_HISTORY(request):
    student = Student.objects.filter(admin=request.user.id)
    for i in student:
        student_id = i.id
        Leave = Student_leave.objects.filter(student_id=student_id)
        context = {
                    "Leave":Leave,
                }
    return render(request,"student/Leave_history.html",context)

def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id

        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            "notification" : notification 
        }
    return render(request,"student/notification.html",context)

def STUDENT_VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_report = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

            # attendance = Attendance.objects.get(subject_id = subject_id)
            attendance_report = Attendance_Report.objects.filter(student_id = student, attendance_date__subject_id = subject_id)
    context = {
        'subjects' : subjects,
        'action': action,
        'get_subject': get_subject,
        'attendance_report':attendance_report,
        }
    return render(request,"student/view_attendance.html",context)

def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin=request.user.id)
    

    result = Student_Result.objects.filter(student_id=student)
    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_mark

        mark = assignment_mark + exam_mark

    context = {
        'result':result,
        'mark':mark,
    }
    return render(request, "student/view_result.html",context)

def studentClasses(request):
    return render(request, "student/classes.html")