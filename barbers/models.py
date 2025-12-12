from django.db import models

# Create your models here.
class Barber(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    POSITION_CHOICES = [
        ('J', 'Junior Barber'),
        ('S', 'Senior Barber'),
        ('M', 'Master Barber')
    ]

    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    birthdate = models.DateField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rating = models.FloatField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.position})"