from django.contrib import admin
from django.urls import path

import barbers.views

urlpatterns = [
    path('', barbers.views.barber_index, name="barber_index"),
    # path('<str:text>/', barbers.views.barber_index, name="barber_index_search"),
    path('list', barbers.views.barber_list),
    path('<int:pk>/', barbers.views.barber_detail, name="barber_detail"),
    path('delete/<int:pk>/', barbers.views.barber_delete),
    path('create', barbers.views.barber_create),
    path('edit/<int:pk>/', barbers.views.barber_update),
]
