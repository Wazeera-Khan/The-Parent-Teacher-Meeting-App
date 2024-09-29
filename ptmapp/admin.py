from django.contrib import admin
from .models import UserProfile, StudentDetail,Attendance,Cie,GPA,ptmNotification,ParentResponse
# admin.site.register(UserProfile)
admin.site.register(StudentDetail)
admin.site.register(Attendance)
admin.site.register(Cie)
admin.site.register(GPA)
admin.site.register(ptmNotification)
admin.site.register(ParentResponse)
admin.site.register(UserProfile)






# from django.contrib import admin
# from .models import Notification
# from .forms import NotificationForm  # Import your NotificationForm

# class NotificationAdmin(admin.ModelAdmin):
#     form = NotificationForm

# admin.site.register(Notification, NotificationAdmin)

