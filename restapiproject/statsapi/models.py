from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
class Student(models.Model):
    id =  models.CharField(
        primary_key=True, 
        max_length=9, 
        validators=[MinLengthValidator(9), MaxLengthValidator(9)]
    )#Rollnos of type 210010026 or cs23bt001 are both length 9. 
    rollno = models.CharField(
        max_length=9, 
        validators=[MinLengthValidator(9), MaxLengthValidator(9)]
    )
    batch = models.IntegerField()
    branch = models.CharField(max_length=50)

    def __str__(self):
        return str(self.rollno)

class Placement(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    ctc = models.FloatField()

    def __str__(self):
        return self.name

class PlacementApplication(models.Model):
    id = models.BigIntegerField(primary_key=True)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    selected = models.BooleanField()

    def __str__(self):
        return f"{self.student.rollno} - {self.placement.name}"
