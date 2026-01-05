from django.contrib import admin
from django.urls import path

import favorites.views

urlpatterns = [
    path('add/<int:barber_id>/<str:return_url>/', favorites.views.add_barber_to_session, name='add_fav_barber'),
]
