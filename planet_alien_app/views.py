from django.http import request
from django.shortcuts import redirect, render
from planet_alien_app.models import *

def index(request):
    context={
        'all_planets': Planet.objects.all(),
    }
    return render(request, 'index.html', context)

def new_planet(request):
    if request.method == "GET":
        return render(request, 'planet.html')
    else:
        Planet.objects.create(name= request.POST['planet_name'], picture= request.POST['planet_pic'])
        return redirect('/')

def delete(request, planet_id):
    Planet.objects.get(id = planet_id).delete()
    return redirect('/')

def planet_info(request, planet_id):
    context={
        'planet': Planet.objects.get(id= planet_id),
    }
    return render(request, 'planet_info.html', context)

def edit(request, planet_id):
    if request.method == "GET":
        context= {
            'planet': Planet.objects.get(id=planet_id),
        }
        return render(request, 'edit.html', context)
    else:
        edit_planet= Planet.objects.get(id=planet_id)
        edit_planet.name = request.POST['planet_name']
        edit_planet.picture= request.POST['planet_pic']
        edit_planet.save()
        return redirect(f"/planet_info/{planet_id}")

def add_alien(request):
    if request.method == "GET":
        context={
            "planets": Planet.objects.all(),
            "all_species": Species.objects.all()
        }
        return render(request, 'add_alien.html', context)
    else:
        host_planet= Planet.objects.get(id= request.POST['planet'])
        alien= Alien.objects.create(name= request.POST['alien_name'], picture= request.POST['alien_pic'], planet=host_planet)
        alien.species.add(Species.objects.get(id= request.POST['species']))
        return redirect(f"/planet_info/{host_planet.id}")