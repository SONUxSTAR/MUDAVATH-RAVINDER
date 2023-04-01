# Generated by Django 4.1.7 on 2023-04-01 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='studentMarksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('sem', models.IntegerField(choices=[(1, 'Semester 1'), (2, 'Semester 2'), (3, 'Semester 3'), (4, 'Semester 4'), (5, 'Semester 5'), (6, 'Semester 6'), (7, 'Semester 7'), (8, 'Semester 8')])),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.studentmainmodel')),
            ],
        ),
        migrations.CreateModel(
            name='studentMarksMainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(choices=[('Mech', 'Mechanical Engineering'), ('csc', 'Computer Science and Engineering'), ('ece', 'Electronics and Communication Engineering'), ('it', 'Information Technology'), ('civil', 'Civil Engineering')], max_length=10)),
                ('marks', models.ManyToManyField(to='API.studentmarksmodel')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='API.studentmainmodel')),
            ],
        ),
    ]
