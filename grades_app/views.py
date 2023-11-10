from django.shortcuts import render
from .models import *
from django.views import View

class HomeView(View):
    def get(self, request):
        students = Students.objects.all()
        student_grades = {}

        for student in students:
            if student.Second_year == 0:
                average_grade = student.First_year
            elif student.Third_year == 0:
                average_grade = (student.First_year + student.Second_year) / 2
            elif student.Fourth_year == 0:
                average_grade = (student.First_year + student.Second_year + student.Third_year) / 3
            else:
                average_grade = (student.First_year + student.Second_year + student.Third_year + student.Fourth_year) / 4
            student_grades[student] = round(average_grade, 2)

        data = {
            'student_grades': student_grades,
        }

        return render(request, 'grades_app/home.html', context=data)



