FAVORITE_BARBERS_KEY = 'favorite_barbers'

def get_favorite_barbers(request):
    return request.session.get(FAVORITE_BARBERS_KEY, [])

def get_count_of_favorite_barbers(request):
    return len(get_favorite_barbers(request))

def add_barber_to_favorites(request, barber_id):
    favoriteIds = get_favorite_barbers(request)
    if barber_id not in favoriteIds:
        favoriteIds.append(barber_id)
        request.session[FAVORITE_BARBERS_KEY] = favoriteIds
    request.session.modified = True

def remove_barber_from_favorites(request, barber_id):
    favoriteIds = get_favorite_barbers(request)
    if barber_id in favoriteIds:
        favoriteIds.remove(barber_id)
        request.session[FAVORITE_BARBERS_KEY] = favoriteIds
    request.session.modified = True