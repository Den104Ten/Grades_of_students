from django.db import models


# Модель базы данных
class Students(models.Model):
    FIO = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    Start_year = models.IntegerField()
    Course = models.IntegerField()
    Group = models.IntegerField()
    First_year = models.IntegerField()
    Second_year = models.IntegerField()
    Third_year = models.IntegerField()
    Fourth_year = models.IntegerField()

    def average_grade(self):
        if self.Second_year == 0:
            total_grades = self.First_year
        elif self.Third_year == 0:
            total_grades = (self.First_year + self.Second_year) / 2
        elif self.Fourth_year == 0:
            total_grades = (self.First_year + self.Second_year + self.Third_year) / 3
        else:
            total_grades = (self.First_year + self.Second_year + self.Third_year + self.Fourth_year) / 4
        return total_grades
