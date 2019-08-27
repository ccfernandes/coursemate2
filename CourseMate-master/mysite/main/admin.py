from django.contrib import admin
from .models import Tutorial, School, Course ,SchoolCourse
from tinymce.widgets import TinyMCE #import tinymce library
from django.db import models 
# Register your models here.
class TutorialAdmin(admin.ModelAdmin):
    #this makes headers for each section or group of sections
    fieldsets = [
        ("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
        ("Content", {"fields":["tutorial_content"]})
    ]

    #overrides the specific textfield with editor widget from tinymce?
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(Tutorial, TutorialAdmin) 
admin.site.register(School)
# admin.site.register(Department)
admin.site.register(SchoolCourse)
admin.site.register(Course)