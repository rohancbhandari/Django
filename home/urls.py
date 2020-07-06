from django.contrib import admin
from django.urls import path
from home import views


urlpatterns = [
    path("",views.index, name='home'),
    path("home",views.home, name='home'),
    path("contact",views.contact, name='contact'),
    path("search",views.search, name='search'),
    path("maindishes",views.maindishes, name='maindishes'),
    path("tacor",views.tacor, name='tacor'),
    path("apricotr",views.apricotr, name='apricotr'),
    path("padr",views.padr, name='padr'),
    path("methir",views.methir, name='methir'),
    path("brownr",views.brownr, name='brownr'),
    path("about",views.about, name='about'),
    path("falr",views.falr, name='falr'),
    path("sandw",views.sandw, name='sandw'),
    path("cutlets",views.cutlets, name='cutlets'),
    path("pestop",views.pestop, name='pestop'),
    path("calzone",views.calzone, name='calzone'),
    path("smoothies",views.smoothies, name='smoothies')
    

]