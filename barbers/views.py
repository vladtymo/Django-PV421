from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm

from barbers.forms import BarberForm
from barbers.models import Barber

# class BarberForm(ModelForm):
#     class Meta:
#         model = Barber
#         fields = "__all__"

def barber_list(request):
    barbers = Barber.objects.all()
    return render(request, "barbers/list.html", {"barbers": barbers})


def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    return render(request, "barbers/detail.html", {"barber": barber})

def barber_create(request):
    if (request.method == "POST"):
        form = BarberForm(request.POST)
        if form.is_valid():
            barber = form.save()
            return redirect(reverse("barber_detail", args=[barber.pk]))
    else:
        form = BarberForm()
    return render(request, "barbers/create.html", {"form": form})


# def barber_create(request):
#     if request.method == "POST":
#         form = BarberForm(request.POST)
#         if form.is_valid():
#             barber = form.save()
#             return redirect(reverse("barber_detail", args=[barber.pk]))
#     else:
#         form = BarberForm()
#     return render(request, "barbers/form.html", {"form": form})


# def barber_update(request, pk):
#     barber = get_object_or_404(Barber, pk=pk)
#     if request.method == "POST":
#         form = BarberForm(request.POST, instance=barber)
#         if form.is_valid():
#             barber = form.save()
#             return redirect(reverse("barber_detail", args=[barber.pk]))
#     else:
#         form = BarberForm(instance=barber)
#     return render(request, "barbers/form.html", {"form": form, "barber": barber})


def barber_delete(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    barber.delete()
    return redirect('/barbers/list')
