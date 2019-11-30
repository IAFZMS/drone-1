from django.urls import path, include

from .views import (
	dron_listing,
	)

urlpatterns = [
    path('drones/', dron_listing, name='dron'),
    ]