from django.shortcuts import render,redirect
from .models import *
from ssa_app.models import Staff_Feedback
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def Take_Attendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff = staff_id)
    session = Session.objects.all()
    action = request.GET.get('action')
    student = None
    get_subject = None
    get_session = None
    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session.objects.get(id = session_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                student = Student.objects.filter(course_id = student_id)

    context = {
        'subject' : subject,
        'session' : session,
        'get_subject' : get_subject,
        'get_session' : get_session,
        'action' : action,
        'student' : student,
    }
    return render(request,"staff/Take_Attendance.html",context)

@login_required(login_url='login')
def Staff_Save_Attendance(request):
    if request.method =='POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')


        get_subject = Subject.objects.get(id = subject_id)
        get_session = Session.objects.get(id = session_id)

        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = attendance_date,
            session_id = get_session,
        )
        attendance.save() 
        for i in student_id:
            stud_id = i 
            int_stud = int(stud_id)

            p_students = Student.objects.get(id = int_stud)
            attendance_report = Attendance_Report(
                student_id = p_students,
                attendance_date = attendance,
            )
            attendance_report.save()
    return redirect('take_attendance')

@login_required(login_url='login')
def Staff_View_Attendance(request):
    staff_id = Staff.objects.get(admin = request.user.id)

    subject = Subject.objects.filter(staff_id = staff_id)
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
    return render(request,"staff/Staff_View_Attendance.html",context)

@login_required(login_url='login')
def Staff_Add_Result(request):
    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    session = Session.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    student = None

    if action is not None:
        if request.method == 'POST':
            subject_id = request.POST.get('subject_id')
            session_id = request.POST.get('session_id')

            get_subject = Subject.objects.get(id = subject_id)
            get_session = Session.objects.get(id = session_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                student = Student.objects.filter(course_id = student_id)

    context = {
        'subjects' : subjects,
        'session' : session,
        'action' : action,
        'get_subject' : get_subject,
        'get_session' : get_session,
        'student' : student,
    }
    return render(request,"staff/Staff_Add_Result.html",context)

@login_required(login_url='login')
def Staff_Save_Result(request):
    if request.method == 'POST':
        subject_id = request.POST.get('subject_id')
        session_id = request.POST.get('session_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        exam_mark = request.POST.get('exam_mark')

        get_student = Student.objects.get(admin = student_id)
        get_subject = Subject.objects.get(id = subject_id)
        
        check_exists = Student_Result.objects.filter(subject_id = get_subject, student_id = get_student).exists()
        if check_exists:
            result = Student_Result.objects.get(subject_id = get_subject, student_id = get_student)
            result.assignment_mark = assignment_mark
            result. exam_mark = exam_mark
            result.save()
            messages.success(request,'Result are successfully updated')
            return redirect('staff_save_result')
        else:
            result = Student_Result(
                student_id = get_student,
                subject_id = get_subject,
                exam_mark = exam_mark,
                assignment_mark = assignment_mark,
            )
            result.save()
            messages.success(request,'Result are successfully added')
    return redirect('staff_add_result')

@login_required(login_url='login')
def Notification(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        Notification = Staff_Notification.objects.filter(staff_id=staff_id)
        context = {
            "Notification":Notification,
        }
    return render(request,'staff/notification.html',context)

@login_required(login_url='login')
def staff_mark_as_done(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staffNotification')

@login_required(login_url='login')
def Staff_Apply_Leave(request):
    return render(request,"staff/Staff_Apply_Leave.html",)

@login_required(login_url='login')
def Staff_Apply_Leave_Save(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_purpose = request.POST.get('leave_purpose')

        staff = Staff.objects.get(admin = request.user.id)
 
        leave = Staff_Leave(
            staff_id = staff,
            s_date = leave_date,
            message = leave_purpose,
        )
        leave.save()
        messages.success(request,'Leave successfully send')
        return redirect('Staff_Apply_Leave_history')
    
@login_required(login_url='login')
def Staff_Apply_Leave_history(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        Leave = Staff_Leave.objects.filter(staff_id=staff_id)
        context = {
                    "Leave":Leave,
                }
    return render(request,"staff/Leave_history.html",context)

@login_required(login_url='login')
def Staff_Feedback(request):
    return render(request,"staff/Feedback.html",)

@login_required(login_url='login')
def StaffFeedback_save(request):
    if request.method == 'POST':
        message = request.POST.get("Feedback")

        # staff = Staff.objects.get(admin = request.user.id)
       

        Feedback = Staff_Feedback(
            # staff_id=staff, 
            feedback=message,
        )
        Feedback.save()
        messages.success(request,'Feedback successfully send')
        return redirect("Staff_Feedback_History")

@login_required(login_url='login')
def sf_History(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
        # Feedback = Staff_Feedback.objects.filter(staff_id=staff_id)
        Feedback = Staff_Feedback.objects.all()
        context = {
                    "Feedback":Feedback,
                }
    return render(request,"staff/Feedback_history.html",context)


def staffClasses(request):
    return render(request, "staff/classes.html")