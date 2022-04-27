from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(),name="home"),
    path('administrator/', views.IndexAdmView.as_view(),name="homeAdm"),
    path('administrator/products/', views.ProductListView.as_view(),name="productsList"),
    path('administrator/products/create', views.ProductsView.as_view(),name="productCreate"),
    path('administrator/products/<int:idp>/update', views.ProductUpdateView.as_view(),name="productUpdate"),
    path('administrator/products/<int:idp>/delete', views.ProductDeleteView.as_view(),name="productDelete"),
    path('products/<int:idp>/details', views.ProductDetailsView.as_view(),name="productDetails"),
    path('products/', views.ProductsGridView.as_view(),name="productsGrid"),
    path('administrator/categories/', views.CategoryListView.as_view(),name="categoriesList"),
    path('administrator/categories/create', views.CategoryView.as_view(),name="categoryCreate"),
    path('administrator/gammes/', views.GammeListView.as_view(),name="gammesList"),
    path('administrator/gammes/create', views.GammeView.as_view(),name="gammeCreate"),
    path('login/', views.loginView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.cart_detail,name='cart_detail'),
    path('cart/add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/remove/<int:product_id>/', views.cart_remove,name='cart_remove'),
    path('cart/update/<int:product_id>/', views.cart_update, name='cart_update'),
    path('order/', views.ClientView.as_view(),name="order"),
]