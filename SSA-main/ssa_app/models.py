from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT'),
    )
    
    user_type = models.CharField(choices=USER, max_length=50, default=1)
    profile_pic = models.ImageField( upload_to='static',)


class Forgot_password(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    forgot_password_token = models.CharField( max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.user.first_name

class Course(models.Model):
    short_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.short_name

class Session(models.Model):
    session_start = models.CharField(max_length=50)
    session_end = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.session_start + " to " + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=7)
    address = models.TextField()
    course_id = models.ForeignKey(Course,on_delete=models.DO_NOTHING)
    session_id = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.admin.first_name + " " + self.admin.last_name
    

class Staff(models.Model):
    admin = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender = models.CharField(max_length=7)
    address = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.admin.first_name
    

class Subject(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True,null = True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.short_name

class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject,on_delete=models.DO_NOTHING)
    attendance_date = models.DateField()
    session_id = models.ForeignKey(Session,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_id.name

class Attendance_Report(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.DO_NOTHING)
    attendance_date = models.ForeignKey(Attendance,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student_id.admin.first_name


class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    short_notification = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default= 0)

    def __str__(self) -> str:
        return self.staff_id.admin.first_name


class Staff_Leave(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    s_date = models.CharField(max_length=20)
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name+ " " +self.staff_id.admin.last_name
    
    
class Staff_Feedback(models.Model):
    staff_id = models.ForeignKey(Staff,on_delete=models.CASCADE)
    feedback = models.TextField()
    reply_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
    
class Student_Feedback(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    feedback = models.TextField()
    reply_feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stucent_id.admin.first_name + " " + self.student_id.admin.last_name

class Student_Result(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject,on_delete=models.CASCADE)
    assignment_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updatted_at = models.DateField(auto_now_add=True)

    def _str_(self):
        return self.student_id.admin.first_name
    
class Student_leave(models.Model):
    student_id =models.ForeignKey(Student,on_delete=models.CASCADE)
    data = models.TextField()
    message = models.TextField()
    status=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def _str_(self) -> str:
        return self.student_id.admin.first_name+""+self.student_id.admin.last_name
    
class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    short_notification = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True,default=0)

    def _str_(self):
        return self.student_id.admin.first_name


class Team(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/TeamImages")
    timing = models.FloatField()
    designation = models.CharField(max_length=100)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/TestimonialImages")
    feedback = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

class Inquiry(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    firstSubject = models.CharField(max_length=200)
    secondSubject = models.CharField(max_length=200)
    message = models.TextField()

class PopularCourses(models.Model):
    courseName = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="images/PopularCoursesImages")
    timing = models.FloatField()
    price = models.IntegerField()
    instructorName = models.CharField(max_length=100)
    time = models.FloatField()
    studentsNumber = models.IntegerField()