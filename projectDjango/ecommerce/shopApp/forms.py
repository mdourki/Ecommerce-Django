from django import forms
from django.db.models import fields
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"
        labels = {
            "nom_prdt":"Nom",
            "description_prdt":"Déscription",
            "marque":"Marque",
            "prix":"Prix",
            "nombre_stock":"Nombre en stock",
            "image_prdt":"Image",
            "categorie":"Catégorie",
            "gamme":"Gamme"
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"
        labels = {
            "nom_cat":"Nom",
            "description_cat":"Déscription"
        }

class GammeForm(forms.ModelForm):
    class Meta:
        model = Gamme
        fields = "__all__"
        labels = {
            "nom_gam":"Nom",
            "description_gam":"Déscription"
        }

class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur")
    password = forms.CharField(widget=forms.PasswordInput,label="Mot de passe")

class ClientForm(forms.Form):
    class Meta:
        model = Client
        fields = "__all__"
        labels = {
            "nom_clt":"Nom",
            "prenom_clt":"Prénom",
            "adresse":"Adresse",
            "email":"Email",
            "ville":"Ville",
            "tel":"Tel",
            "img_clt":"Image"
        }
