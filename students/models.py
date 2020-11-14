from django.db import models

# Creation of student model for DB
class Student(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField('DOB')
    banner_id = models.CharField(max_length=200)
    course = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        ##^ Sets record name = student.name;
        ##^ Still works if not included
        ##^ Makes admin page more readable
