from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import ModelForm

from barbers.forms import BarberForm
from barbers.models import Barber
from django.contrib import messages

def barber_list(request):
    barbers = Barber.objects.all()

    return render(request, "barbers/list.html", {"barbers": barbers})

def barber_index(request):
    barbers = Barber.objects.all()

    return render(request, "barbers/index.html", {"barbers": barbers})

def barber_detail(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    return render(request, "barbers/detail.html", {"barber": barber})

# метод додавання нового барбера
def barber_create(request):
    # якщо запит є POST, тоді додаємо елемент в базу
    if (request.method == "POST"):
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            barber = form.save()
            messages.success(request, f"Barber {barber.name} has been created successfully")
            return redirect(reverse("barber_detail", args=[barber.pk]))
    else:
        # якщо запит не є POST, тоді показуємо порожню форму
        form = BarberForm()
    return render(request, "barbers/create.html", {"form": form})

def barber_update(request, pk):
    # шукаємо барбера за id
    barber = get_object_or_404(Barber, pk=pk)

    if request.method == "POST":
        # створюємо форму з даними з запиту та існуючого барбера
        form = BarberForm(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            # зберігаємо зміни в базу
            barber = form.save()
            messages.success(request, f"Barber {barber.name} has been updated successfully")
            return redirect(reverse("barber_detail", args=[barber.pk]))
    else:
        # створюємо форму з даними знайденого барбера
        form = BarberForm(instance=barber)

    return render(request, "barbers/edit.html", {"form": form})


def barber_delete(request, pk):
    barber = get_object_or_404(Barber, pk=pk)
    barber.delete()
    messages.error(request, f"Barber {barber.name} has been deleted successfully")
    return redirect('/barbers/list')
