from django.contrib import admin
from django.urls import path

import home.views

urlpatterns = [
    path('', home.views.home, name='home'),
    path('book', home.views.book_service, name='book'),
]
