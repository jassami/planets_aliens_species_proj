from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_planet', views.new_planet),
    path('delete/<int:planet_id>', views.delete),
    path('planet_info/<int:planet_id>', views.planet_info),
    path('edit/<int:planet_id>', views.edit),
    path('add_alien', views.add_alien),
]
