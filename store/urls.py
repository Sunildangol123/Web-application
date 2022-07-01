from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('index', views.index, name="index"),
    path('pizza', views.pizza, name="pizza"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.register, name="register"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]