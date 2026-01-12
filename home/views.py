from datetime import datetime
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView

from barbers.models import Barber, Booking

# Create your views here.
def home(request):
    bookings = Booking.objects.all()  
    return render(request, "home/index.html", {"bookings": bookings})

def book_service(request):

    Booking.objects.create(
        barber_id=Barber.objects.first().id,
        customer_name="Vlad",
        appointment_date="2026-01-13 14:00",
        contact_phone="+1234567890"
    )
    return redirect('home')

class CustomLoginView(LoginView):
    # template_name = 'admin/login.html'
    # authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Add your authentication logic here
        return super().form_valid(form)