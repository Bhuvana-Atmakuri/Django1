from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.ho, name="ho"),
    path('order',views.order,name="order"),
    path('About',views.About,name="About"),
    path('con',views.con,name="con"),
    path('sign',views.sign,name="sign"),
    path('activate/<uid64>/<token>',views.activate,name='activate'),
    path('orderin',views.orderin,name="orderin"),
    path('orderin2', views.orderin2, name="orderin2"),
    path('orderin3', views.orderin3, name="orderin3"),
    path('orderin4', views.orderin4, name="orderin4"),
    path('cart', views.cart, name="cart"),
path('orderin5', views.orderin5, name="orderin5"),
path('orderin6', views.orderin6, name="orderin6"),
]
