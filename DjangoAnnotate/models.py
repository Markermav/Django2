from django.db import models

# Create your models here.

class StudentMarks(models.Model):
    rollno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    totalPercentage = models.FloatField()
    mathMarks = models.IntegerField()
    scienceMaths =  models.IntegerField()
    languageMarks = models.IntegerField()

    def __str__(self):
        return self.name