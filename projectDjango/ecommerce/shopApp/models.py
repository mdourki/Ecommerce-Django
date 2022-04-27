from django.db import models
from django import forms
from django.db.models.base import Model

# Create your models here.

class Client(models.Model):
    nom_clt=models.CharField(max_length=100)
    prenom_clt=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    email=models.EmailField()
    ville=models.CharField(max_length=100)
    tel=models.CharField(max_length=20)
    img_clt=models.ImageField(upload_to="clients/")

    def __str__(self):
        return self.nom_clt

class Categorie(models.Model):
    nom_cat=models.CharField(max_length=100)
    description_cat=models.TextField()

    def __str__(self):
          return self.nom_cat

class Gamme(models.Model):
    nom_gam=models.CharField(max_length=100)
    description_gam=models.TextField()

    def __str__(self):
          return self.nom_gam

class Commande(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    adresse_livraison= models.CharField(max_length=100)
    code_postal = models.CharField(max_length=20)
    date_cmd = models.DateField()

class Produit(models.Model):
    nom_prdt=models.CharField(max_length=100)
    description_prdt=models.TextField()
    marque=models.CharField(max_length=100)
    prix=models.FloatField()
    nombre_stock=models.IntegerField()
    image_prdt=models.ImageField(upload_to = "products/")
    categorie=models.ForeignKey(Categorie,on_delete=models.CASCADE)
    gamme=models.ForeignKey(Gamme,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom_prdt

class user(models.Model):
    nom_usr=models.CharField(max_length=100)
    prenom_usr=models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

