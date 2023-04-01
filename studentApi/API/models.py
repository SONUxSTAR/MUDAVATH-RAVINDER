from django.db import models


class StudentMainModel(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=255)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='images/')

class studentMarksModel(models.Model):
    SEM_CHOICES = [
        (1, 'Semester 1'),
        (2, 'Semester 2'),
        (3, 'Semester 3'),
        (4, 'Semester 4'),
        (5, 'Semester 5'),
        (6, 'Semester 6'),
        (7, 'Semester 7'),
        (8, 'Semester 8'),
    ]

    student = models.ForeignKey(StudentMainModel, on_delete=models.CASCADE)
    marks = models.IntegerField()
    sem = models.IntegerField(choices=SEM_CHOICES)

class studentMarksMainModel(models.Model):
    BRANCH_CHOICES = [
        ('Mech', 'Mechanical Engineering'),
        ('csc', 'Computer Science and Engineering'),
        ('ece', 'Electronics and Communication Engineering'),
        ('it', 'Information Technology'),
        ('civil', 'Civil Engineering'),
    ]

    student = models.OneToOneField(StudentMainModel, on_delete=models.CASCADE)
    marks = models.IntegerField(studentMarksModel)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)