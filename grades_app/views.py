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



class BooksView(View):

    def get(self, request):
        # Жанр: Роман
        roman = Books.objects.filter(genre='Роман')  # далее вывести список романов, отсортировав по популярности
        fantastic = Books.objects.filter(genre='Фантастика')
        fantasy = Books.objects.filter(genre='Фэнтези')
        triller = Books.objects.filter(genre='Триллер')
        filosof_roman = Books.objects.filter(genre='Философский роман')
        child_lit = Books.objects.filter(genre='Детская литература')
        data = {'roman': sorted(roman, key=lambda x: x.grade_popularity, reverse=True),
                'fantastic': sorted(fantastic, key=lambda x: x.grade_popularity, reverse=True),
                'fantasy': sorted(fantasy, key=lambda x: x.grade_popularity, reverse=True),
                'triller': sorted(triller, key=lambda x: x.grade_popularity, reverse=True),
                'filosof_roman': sorted(filosof_roman, key=lambda x: x.grade_popularity, reverse=True),
                'child_lit': sorted(child_lit, key=lambda x: x.grade_popularity, reverse=True)}
        return render(request, 'grades_app/book.html', context=data)






