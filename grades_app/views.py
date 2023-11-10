from django.shortcuts import render
from .models import *
from django.views import View


# Представление главной странички home
class HomeView(View):
    def get(self, request):
        students = Students.objects.all()  # получаем все объекты из базы данных

        # создаем список студентов с средней оценкой
        student_grades = []
        for student in students:
            if student.Second_year == 0:
                average_grade = student.First_year
            elif student.Third_year == 0:
                average_grade = (student.First_year + student.Second_year) / 2
            elif student.Fourth_year == 0:
                average_grade = (student.First_year + student.Second_year + student.Third_year) / 3
            else:
                average_grade = (student.First_year + student.Second_year + student.Third_year + student.Fourth_year) / 4
            student_grades.append({'student': student, 'grade': round(average_grade, 2)})

        # сортируем список студентов по средней оценке
        sorted_student_grades = sorted(student_grades, key=lambda x: x['grade'], reverse=True)

        # передаем отсортированный список в шаблон
        data = {
            'student_grades': sorted_student_grades,
        }

        return render(request, 'grades_app/home.html', context=data)




