from django.shortcuts import render
from django.contrib.auth.views import LoginView

# Create your views here.
def home(request):
    return render(request, "home/index.html")

class CustomLoginView(LoginView):
    # template_name = 'admin/login.html'
    # authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # Add your authentication logic here
        return super().form_valid(form)