from django.db import models
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator

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
    photo = models.ImageField(upload_to='barber_photos/', blank=True, null=True)
    experience = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(60)])
    birthdate = models.DateField()
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    rating = models.FloatField(default=0)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.position})"
    
class Booking(models.Model):
    barber = models.ForeignKey(Barber, on_delete=models.CASCADE, related_name='bookings')
    customer_name = models.CharField(max_length=100)
    appointment_date = models.DateTimeField()
    contact_phone = models.CharField(max_length=20)

    def __str__(self):
        return f"Booking for {self.customer_name} with {self.barber.name} on {self.appointment_date}"