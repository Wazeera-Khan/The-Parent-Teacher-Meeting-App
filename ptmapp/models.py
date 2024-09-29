
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    parent_name = models.CharField(max_length=100)
    parent_phone_number = models.CharField(max_length=15)  # Adjust field as per your needs
    student_name = models.CharField(max_length=100)
    student_usn = models.CharField(max_length=50)  # Adjust field as per your needs
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.student_usn  # Display name in Django admin or shell
    
class StudentDetail(models.Model):
   
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    usn = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    semester = models.IntegerField()
    # Add other fields here

    def __str__(self):
        return self.usn
    
class Attendance(models.Model):
    student_detail = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=8)  # Assuming subject code is unique identifier
    attendance_percentage = models.FloatField()

    def __str__(self):
        return f'{self.student_detail.usn} - {self.subject_code} - Attendance'
    
class Cie(models.Model):
    student_detail = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    subject_code = models.CharField(max_length=8)  # Assuming subject code is unique identifier
    cie3 = models.FloatField(null=True,blank=True,default="N/A")
    cie1 = models.FloatField(null=True,blank=True,default="N/A")
    cie2 = models.FloatField(null=True,blank=True,default="N/A")

    def __str__(self):
        return f'{self.student_detail.usn} - {self.subject_code} - CIE'
    
class GPA(models.Model):
    student_detail = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    semester = models.IntegerField()
    gpa = models.FloatField(null=True, blank=True)
   

    def __str__(self):
        return f'{self.student_detail.usn} - Semester {self.semester} - GPA: {self.gpa}'
    

from django.db import models

class ptmNotification(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    meeting_datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class ParentResponse(models.Model):
    notification = models.ForeignKey(ptmNotification, on_delete=models.CASCADE)
    student_detail = models.OneToOneField(StudentDetail, on_delete=models.CASCADE)

    response = models.BooleanField()  # True for accept, False for decline

    def __str__(self):
        return f'{self.student_detail.usn} - {self.notification.title} - {self.response}'