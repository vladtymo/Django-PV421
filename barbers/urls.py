from django.contrib import admin
from django.urls import path

import barbers.views

urlpatterns = [
    path('list', barbers.views.barber_list),
    path('<int:pk>/', barbers.views.barber_detail),
    # path('delete/<int:pk>/', barbers.views.barber_delete),

]
