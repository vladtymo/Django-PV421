from django.contrib import admin
from django.urls import path

import barbers.views

urlpatterns = [
    path('list', barbers.views.barber_list),
    path('<int:pk>/', barbers.views.barber_detail, name="barber_detail"),
    path('delete/<int:pk>/', barbers.views.barber_delete),
    path('create', barbers.views.barber_create),
    path('edit/<int:pk>/', barbers.views.barber_update),
]
