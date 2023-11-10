from django.test import TestCase
from .views import *
from .models import *
from django.urls import reverse


# Тесты!!!

# Первый тест проверяет правильный ли статус код выдает страничка

# Второй тест проверяет корректно ли отображаются студенты на страничке

# Третий тест проверяет корректно ли вычисляется средний балл для студентов

# Во всех тестах были созданы искуственные студенты для проверки правильности обработки данных

class TestHomeView(TestCase):
    
    # 1 Test
    def test_HomeView(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    # 2 Test
    def test_student_list_displayed(self):
        # Test_examples
        student1 = Students.objects.create(FIO='Карасев Марк Даниэльевич', DOB='23.08.2004', Start_year=2022, Course=2, Group=8294, First_year=5, Second_year=3, Third_year=0, Fourth_year=0)
        
        url = reverse('home')
        response = self.client.get(url)
        
        self.assertTemplateUsed(response, 'grades_app/home.html')
        self.assertContains(response, student1.FIO)
        
    # 3 Test
    def test_average_grade_calculation(self):
        # Test examples
        student1 = Students.objects.create(FIO='Карасев Марк Даниэльевич', DOB='23.08.2004', Start_year=2022, Course=2,
                                           Group=8294, First_year=5, Second_year=3, Third_year=0, Fourth_year=0)

        url = reverse('home')
        response = self.client.get(url)

        self.assertTemplateUsed(response, 'grades_app/home.html')
        # Проверяем, что средняя оценка для каждого студента вычисляется правильно. До двух знаков после запятой
        self.assertAlmostEqual(student1.average_grade(), 4, places=2)


