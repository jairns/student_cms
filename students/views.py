from django.shortcuts import render

from .models import Student

# Get students and dispaly them
def index(request):
    latest_student_list = Student.objects.all() # Getting the Student objects from the model
    context = {'latest_student_list': latest_student_list} # Storing data in context variable
    return render(request, 'students/index.html', context) # Passing context to index.html