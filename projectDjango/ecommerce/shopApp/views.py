from django.shortcuts import redirect, render
from django.views import View
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from ecommerce import settings

# Create your views here.

class ProductListView(View):
    def get(self,request):
        produits=Produit.objects.all()
        return render(request,"products_list.html",{'produits':produits})

class CategoryListView(View):
    def get(self,request):
        categories=Categorie.objects.all()
        return render(request,"categories_list.html",{'categories':categories})

class ProductsView(View):
    def get(self,request):
        form=ProductForm()
        return render(request,"product_form.html",{'form':form})
    def post(self,request):
        form=ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("productsList")

class ProductsGridView(View):
    def get(self,request):
        produits=Produit.objects.all()
        return render(request,"products_grid.html",{'produits':produits})

class ProductUpdateView(View):
    def get(self,request,idp):
        produit=Produit.objects.get(id=idp)
        form=ProductForm(instance=produit)
        return render(request,"product_form.html",{'form':form})
    def post(self,request,idp):
        produit=Produit.objects.get(id=idp)
        form=ProductForm(request.POST,request.FILES,instance=produit)
        if form.is_valid():
            form.save()
        return  redirect("productsList")

class ProductDeleteView(View):
    def get(self,request,idp):
        return render(request,"product_delete.html",{})
    def post(self,request,idp):
        produit=Produit.objects.get(id=idp)
        produit.delete()
        return  redirect("productsList")

class ProductDetailsView(View):
    def get(self,request,idp):
        produit=Produit.objects.get(id=idp)
        return render(request,"product_details.html",{'produit':produit})

class CategoryView(View):
    def get(self,request):
        form=CategoryForm()
        return render(request,"category_form.html",{'form':form})
    def post(self,request):
        form=CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("categoriesList")

class GammeListView(View):
    def get(self,request):
        gammes=Gamme.objects.all()
        return render(request,"gammes_list.html",{'gammes':gammes})

class GammeView(View):
    def get(self,request):
        form=GammeForm()
        return render(request,"gamme_form.html",{'form':form})
    def post(self,request):
        form=GammeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("gammesList")

class IndexView(View):
    def get(self,request):
        return render(request,"index.html",{})

class IndexAdmView(View):
    def get(self,request):
        return render(request,"index_adm.html",{})

class loginView(View):
    def get(self,request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('productsList')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        return redirect("home")

def user_logout(request):
    logout(request)
    return redirect('home')

def cart_add(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID,{})
    produit = Produit.objects.get(id=product_id)
    produit_id = str(produit.id)
    if produit_id not in cart:
            cart[produit_id] = {'quantity': 1,'price': produit.prix}

    request.session[settings.CART_SESSION_ID]=cart

    return redirect('productsGrid')

def cart_update(request, product_id):
    cart = request.session.get(settings.CART_SESSION_ID)
    produit = Produit.objects.get(id=product_id)
    cart[str(product_id)]['quantity']=request.POST.get('quantity')
    request.session[settings.CART_SESSION_ID]=cart

    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart=request.session.get(settings.CART_SESSION_ID)
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session[settings.CART_SESSION_ID]=cart
    return redirect('cart_detail')

def cart_detail(request):
    cart = request.session.get(settings.CART_SESSION_ID,{})
    cart_total_price=0

    for key,val in cart.items():
        produit = Produit.objects.get(id=key)
        cart[str(produit.id)]['product']=produit
        cart[str(produit.id)]['price'] = produit.prix
        cart[str(produit.id)]['total_price'] = float(cart[str(produit.id)]['price']) * float(cart[str(produit.id)]['quantity'])
        cart_total_price+=cart[str(produit.id)]['total_price']
    
    return render(request, 'cart_detail.html', {'cart': cart,'cart_total_price':cart_total_price})

class ClientView(View):
    def get(self,request):
        form=ClientForm()
        return render(request,"client_form.html",{'form':form})
    def post(self,request):
        form=ClientForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect("productsGrid")