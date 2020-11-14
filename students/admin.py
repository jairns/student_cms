from django.contrib import admin

# Importing Student Model
from .models import Student

admin.site.site_header = 'Student Admin'
admin.site.site_title = 'Student Admin Area'
admin.site.index_title = 'Welcome to the Student Admin Area'


#Registering the models
admin.site.register(Student)
