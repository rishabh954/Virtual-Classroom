from django.contrib import admin
from django.urls import path
from . import views,HOD_views,staff_views,student_views
from django.contrib.auth import views as auth_views


# Django admin 
admin.site.site_header = "Smart Start Academy"
admin.site.site_title = "welcome to again!"
admin.site.index_title = "Learning for Everyone"

urlpatterns = [

    path('',views.home,name="index.html"),
    path('team',views.team,name="team.html"),
    path('contact',views.contact,name="contact.html"),
    path('about',views.about,name="about.html"),
    path('error',views.error,name="error.html"),
    path('courses',views.courses,name="courses.html"),
    path('contact',views.contact,name="contact.html"),
    path('testimonial',views.testimonial,name="testimonial.html"),
    path('register',views.register,name="register.html"),


    # login path
    path('login',views.homelogin,name="login"),
    path('dologin',views.dologin,name="dologin"),
    path('dologout',views.dologout,name="dologout"),
    # path('forgot_password',views.forgot_password,name="forgot_password"),
    # path('change_password',views.change_password,name="change_password"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"),name="password_reset_complete"),


    # profile update
    path('Hod/Home',views.hod_home,name="hod_home"),
    path('profile',views.profile,name="profile"),
    path('profile/update',views.profile_update,name="profile_update"),


    # hod panel
    path('Hod/Student/Add',HOD_views.AddStudent,name="AddStudent"), 
    path('Hod/Student/View',HOD_views.ViewStudent,name="ViewStudent"),
    path('Hod/Student/Update',HOD_views.UpdateStudent,name="UpdateStudent"),
    path('Hod/Student/Edit/<str:id>',HOD_views.EditStudent,name="EditStudent"),
    path('Hod/Student/Delete/<str:admin>',HOD_views.DeleteStudent,name="DeleteStudent"),


    path('Hod/Course/Add',HOD_views.AddCourse,name="AddCourse"),
    path('Hod/Course/View',HOD_views.ViewCourse,name="ViewCourse"),
    path('Hod/Course/Edit/<str:id>',HOD_views.EditCourse,name="EditCourse"),
    path('Hod/Course/Update',HOD_views.UpdateCourse,name="UpdateCourse"),
    path('Hod/Course/Delete/<str:id>',HOD_views.DeleteCourse,name="DeleteCourse"),


    path('Hod/Staff/Add',HOD_views.AddStaff,name="AddStaff"),
    path('Hod/Staff/View',HOD_views.ViewStaff,name="ViewStaff"),
    path('Hod/Staff/Edit/<str:id>',HOD_views.EditStaff,name="EditStaff"),
    path('Hod/Staff/Update',HOD_views.UpdateStaff,name="UpdateStaff"),
    path('Hod/Staff/Delete/<str:admin>',HOD_views.DeleteStaff,name="DeleteStaff"),
    



    path('Hod/Subject/Add',HOD_views.AddSubject,name="AddSubject"),
    path('Hod/Subject/View',HOD_views.ViewSubject,name="ViewSubject"),
    path('Hod/Subject/Edit/<str:id>',HOD_views.EditSubject,name="EditSubject"),
    path('Hod/Subject/Update',HOD_views.UpdateSubject,name="UpdateSubject"),
    path('Hod/Subject/Delete/<str:id>',HOD_views.DeleteSubject,name="DeleteSubject"),


    path('Hod/Session/Add',HOD_views.AddSession,name="AddSession"),
    path('Hod/Session/View',HOD_views.ViewSession,name="ViewSession"),
    path('Hod/Session/Edit/<str:id>',HOD_views.EditSession,name="EditSession"),
    path('Hod/Session/Update',HOD_views.UpdateSession,name="UpdateSession"),
    path('Hod/Session/Delete/<str:id>',HOD_views.DeleteSession,name="DeleteSession"),


    path('Hod/Student/Student_notification/<str:id>',HOD_views.StudentSendnotification,name="Studentsendnotification"),
    path('Hod/Student/Save_student',HOD_views.Save_student,name="Save_student"),
    path('Hod/Student/Student_status',HOD_views.Student_status,name="Student_status"),


    # student  leave
    path('Hod/Student/leave_view',HOD_views.Student_leave_view,name="Student_leave_view"),
    path('Hod/Student/leave_approve/<str:id>',HOD_views.Student_leave_approve,name="Student_leave_approve"),
    path('Hod/Student/leave_disapprove/<str:id>',HOD_views.Student_leave_disapprove,name="Student_leave_disapprove"),

    path('Hod/View_Attendance',HOD_views.Student_view_attendance, name="Student_view_attendance"),

    # staff  leave
    path('Hod/Staff/leave_view',HOD_views.Staff_leave_view,name="Staff_leave_view"),
    path('Hod/Staff/leave_approve/<str:id>',HOD_views.Staff_leave_approve,name="Staff_leave_approve"),
    path('Hod/Staff/leave_disapprove/<str:id>',HOD_views.Staff_leave_disapprove,name="Staff_leave_disapprove"),

    # staff task
    path('Hod/Student/StaffSendNotification/<str:id>',HOD_views.StaffSendNotification,name="StaffSendNotification"),
    path('Hod/Staff/Save_staff',HOD_views.Save_staff,name="Save_staff"),
    path('Hod/Student/Staff_status',HOD_views.Staff_status,name="Staff_status"),



    # staff url 
    path('Staff/Notification',staff_views.Notification,name="staffNotification"),
    path('Staff/mark_as_done/<str:status>',staff_views.staff_mark_as_done,name="staff_mark_as_done"),
    
    # staff leaves
     path('Staff/Staff_Apply_Leave',staff_views.Staff_Apply_Leave,name="staff_apply_leave"),
     path('Staff/Staff_Apply_Leave_history',staff_views.Staff_Apply_Leave_history,name="Staff_Apply_Leave_history"),
     path('Staff/Staff_Apply_Leave_Save',staff_views.Staff_Apply_Leave_Save,name="staff_apply_leave_save"),


    # staff feedback
    path('Staff/Feedback',staff_views.Staff_Feedback,name="Staff_Feedback"),
    path('Staff/Feedback/save',staff_views.StaffFeedback_save,name="Staff_Feedback_save"),
    path('Staff/Feedback_history',staff_views.sf_History,name="Staff_Feedback_History"),
   
#     # staff attendance
    path('Staff/Take_Attendance',staff_views.Take_Attendance,name="take_attendance"),
    path('Staff/Staff_View_Attendance',staff_views.Staff_View_Attendance,name="staff_view_attendance"),
    path('Staff/Staff_Save_Attendance',staff_views.Staff_Save_Attendance,name="staff_save_attendance"),

#     #staff result
    path('Staff/Staff_Add_Result',staff_views.Staff_Add_Result,name="staff_add_result"),
    path('Staff/Staff_Save_Result',staff_views.Staff_Save_Result,name="staff_save_result"),      

    path("Staff/class", staff_views.staffClasses, name="staffClasses"),

    
    # student url
    path('Student/Notification',student_views.Notification,name="studentNotification"),
    path('Student/mark_as_done/<str:status>',student_views.student_mark_as_done,name="student_mark_as_done"),
    path("student/apply_for_leave", student_views.STUDENT_LEAVE,name='student_leave'),
    path("student/leave_save", student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),
    path("student/leave_history", student_views.STUDENT_LEAVE_HISTORY,
    name="student_leave_history"),
    
    path("student/view_attendance/", student_views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),

    path("student/view_result", student_views.VIEW_RESULT, name="view_result"),

    path("student/class", student_views.studentClasses, name="studentClasses"),
    
]