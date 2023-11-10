from django.db import models


class Students(models.Model):
    FIO = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    Start_year = models.DateField()
    Course = models.IntegerField()
    Group = models.IntegerField()
    First_year = models.IntegerField()
    Second_year = models.IntegerField()
    Third_year = models.IntegerField()
    Fourth_year = models.IntegerField()


