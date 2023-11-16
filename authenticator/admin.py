from django.contrib import admin
from .models import CustomUser, CustomUserManager, Question, Test, TestResult, Class


# Register your models here.

# admin.site.register( Student, UserAdmin)
admin.site.register(CustomUser)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(Class)
