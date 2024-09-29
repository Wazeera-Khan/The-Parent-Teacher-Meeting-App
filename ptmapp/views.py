from django.shortcuts import render,redirect,get_object_or_404
from .models import  UserProfile,StudentDetail,Attendance,Cie,GPA
from django.contrib import messages
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login as django_login
from django.http import HttpResponseBadRequest

def register(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to UserProfile model
            messages.success(request, 'Registration successful!')  # Add success message
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserProfileForm()
    
    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        usn = request.POST.get('usn')
        password = request.POST.get('password')
        
        if usn and password:
            # Check if the provided USN exists in the database
            if UserProfile.objects.filter(student_usn=usn).exists():
                # Get the user profile
                user_profile = UserProfile.objects.get(student_usn=usn)
                
                # Check if the password matches
                if user_profile.password == password:
                    request.session['logged_in_usn'] = usn
                    # Redirect to drpdwn.html after successful login
                    return redirect('drpdwn')  # Replace 'drpdwn' with your URL name for drpdwn.html
                else:
                    messages.error(request, 'Invalid password. Please try again.')
            else:
                messages.error(request, 'This USN is not registered.')
        else:
            messages.error(request, 'Please provide both USN and password.')
    
    return render(request, 'login.html')

def drpdwn(request):
    if request.method == 'POST':
        semester = request.POST.get('semester')
        usn = request.session.get('logged_in_usn')
        
        if semester and usn:
            # Check if the semester exists for the logged-in USN in StudentDetail model
            if StudentDetail.objects.filter(usn=usn, semester=semester).exists():
                # Redirect to home.html on successful selection
                return redirect('home')  # Replace 'home' with your URL name for home.html
            else:
                error_message = 'Semester not found for this USN.'
                return render(request, 'drpdwn.html', {'error_message': error_message})
        else:
            error_message = 'Invalid semester selection.'
            return render(request, 'drpdwn.html', {'error_message': error_message})
    
    return render(request, 'drpdwn.html')
    
def home(request):
    usn = request.session.get('logged_in_usn')
    if usn:
        student = StudentDetail.objects.get(usn=usn)
        context = {
            'usn': student.usn,
            'name': student.name,
            'semester': student.semester,
        }
        return render(request, 'home.html', context)
    else:
        messages.error(request, 'User session not found.')
        return redirect('login')


def attendance(request):
    usn = request.session.get('logged_in_usn')
    if usn:
        # Fetch the student detail based on the logged-in USN
        student_detail = StudentDetail.objects.get(usn=usn)
        
        # Fetch attendance records related to this student detail
        attendances = Attendance.objects.filter(student_detail=student_detail)

        context = {
            'student_detail': student_detail,
            'attendances': attendances,
        }

        return render(request, 'attendance.html', context)
    else:
        messages.error(request, 'User session not found.')
        return redirect('login')
    

def cie(request):
    usn = request.session.get('logged_in_usn')
    if usn:
        
            student = StudentDetail.objects.get(usn=usn)
            cie_records = Cie.objects.filter(student_detail=student)
            context = {
                'name': student.name,
                'usn': student.usn,
                'cie_records': cie_records,
            }
            return render(request, 'cie.html', context)
      
    else:
        # Handle case where user is not logged in
        messages.error(request, 'User session not found.')
        return redirect('login')


from django.db.models import Avg

def gpa(request):
    usn = request.session.get('logged_in_usn')
    if usn:
        
            student = StudentDetail.objects.get(usn=usn)
            gpa_records = GPA.objects.filter(student_detail=student)
            
            # Calculate average GPA across all semesters
            average_gpa = GPA.objects.filter(student_detail=student).aggregate(Avg('gpa'))['gpa__avg']
            
            context = {
                'name': student.name,
                'usn': student.usn,
                'gpa_records': gpa_records,
                'average_gpa': average_gpa,
            }
            
            return render(request, 'gpa.html', context)
        
        
    
    else:
        messages.error(request, 'User session not found.')
        return redirect('login')


from django.utils import timezone
from .models import ptmNotification, ParentResponse
from .forms import ParentResponseForm




# def save_response(request):
#     usn = request.session.get('logged_in_usn')
#     notification = get_object_or_404(ptmNotification, pk=notification_id)
#     notification_id = request.POST.get('notification_id')

   
#     response_value = request.POST.get('response')

#     if response_value in ['0', '1']:  # Ensure response_value is valid
#         usn = request.session.get('logged_in_usn')
#         response = response_value == '1'  # True for accept, False for decline

#         # Create or update ParentResponse object
#         ParentResponse.objects.create(
#             notification = notification,
#             response = response
#         )

#         return redirect('home')  # Redirect to a success page or dashboard
#     else:
#         return HttpResponseBadRequest('Invalid form submission.')

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import ptmNotification, ParentResponse
from .forms import ParentResponseForm

def save_response(request):
    if request.method == 'POST':
        form = ParentResponseForm(request.POST)
        if form.is_valid():
            response = form.cleaned_data['response']
            notification_id = form.cleaned_data['notification_id']  # Assuming notification_id is passed via form data

            # Fetch the notification object
            notification = get_object_or_404(ptmNotification, pk=notification_id)

            # Assuming you have the logged in user's profile associated with the response
            user_profile = request.user.userprofile

            # Save the response
            parent_response = ParentResponse.objects.create(
                notification=notification,
                user_profile=user_profile,
                response=response
            )

            # Optionally, you might want to redirect to a success page or back to the notification form
            return HttpResponseRedirect(reverse('home'))
    else:
        form = ParentResponseForm()

    # Handle cases where form is not valid or initial GET request
    return render(request, 'register.html', {'form': form})


def notification_list(request):
    notifications = ptmNotification.objects.all()
    return render(request, 'notification_list.html',{'notifications': notifications})
def parent_response_form(request):
    notifications = ptmNotification.objects.all()
    return render(request, 'respond_notification.html',{'notifications': notifications})













