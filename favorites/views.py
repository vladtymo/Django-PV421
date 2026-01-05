from django.shortcuts import redirect

from favorites.favorites import add_barber_to_favorites, add_barber_to_favorites

def add_barber_to_session(request, barber_id, return_url):
    add_barber_to_favorites(request, barber_id)
    return redirect(return_url)
