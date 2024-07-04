from django.contrib import admin
from .models import PythonBook,Users,Comment
admin.site.register(PythonBook)
# admin.site.register(User)
admin.site.register(Users)
admin.site.register(Comment)
# Register your models here.
