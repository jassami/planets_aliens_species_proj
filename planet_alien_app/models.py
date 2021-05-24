from django.db import models

class Planet(models.Model):
    name= models.CharField(max_length=45)
    picture= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now=True)

class Alien(models.Model):
    name= models.CharField(max_length=45)
    picture= models.CharField(max_length=255)
    planet= models.ForeignKey(Planet, related_name="aliens", on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now=True)


class Species(models.Model):
    name= models.CharField(max_length=45)
    aliens= models.ManyToManyField(Alien, related_name='species')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
