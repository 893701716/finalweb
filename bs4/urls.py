from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='index'),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('coldemo/',views.coldemo,name='coldemo'),
    path('menu/',views.menu,name='menu'),
    path('mainpage/',views.mainpage,name='mainpage'),
    path("more/",views.more,name='more'),
    path("nav/",views.nav,name='nav'),
    path("contact/",views.contact,name='contact'),
]
