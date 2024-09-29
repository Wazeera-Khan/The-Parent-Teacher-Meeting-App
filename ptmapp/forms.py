# forms.py

from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['parent_name', 'parent_phone_number', 'student_name', 'student_usn', 'password']

    def clean_student_usn(self):
        usn = self.cleaned_data['student_usn']
        if UserProfile.objects.filter(student_usn=usn).exists():
            raise forms.ValidationError("This USN is already registered.")
        return usn

    def clean_parent_phone_number(self):
        phone = self.cleaned_data['parent_phone_number']
        if UserProfile.objects.filter(parent_phone_number=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone


# In forms.py
from django import forms
from .models import ParentResponse

class ParentResponseForm(forms.ModelForm):
    class Meta:
        model = ParentResponse
        fields =['notification', 'response']
        
