from django.db import models

# Create your models here.

class Teacher(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    description = models.TextField()
    birth_date = models.DateTimeField('birth date ')
    entry_date = models.DateTimeField('entry date ')
    photo = models.CharField(max_length=20)
    idBirthCertificate = models.CharField(max_length=20)


class TelTeacher(models.Model):
    telTeacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    telNrTeacher = models.CharField(max_length=30)
