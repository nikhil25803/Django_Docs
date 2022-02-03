from django.contrib import admin

# Register your models here.

from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender', 'locality', 'city', 'pin', 'mobile', 'job_city', 'profile_image', 'my_file']
