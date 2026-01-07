from django.shortcuts import redirect, render

from barbers.models import Barber
from favorites.favorites import add_barber_to_favorites, add_barber_to_favorites, get_favorite_barbers, remove_barber_from_favorites


def index(request):
    barbers = Barber.objects.all()
    favoriteIds = get_favorite_barbers(request)

    barbers = [barber for barber in barbers if barber.id in favoriteIds]
    return render(request, "favorites/index.html", {"barbers": barbers})

def add_barber(request, barber_id, return_url):
    add_barber_to_favorites(request, barber_id)
    return redirect(return_url)

def remove_barber(request, barber_id, return_url):
    remove_barber_from_favorites(request, barber_id)
    return redirect(return_url)
