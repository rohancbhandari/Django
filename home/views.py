from django.shortcuts import render, HttpResponse
from home import models
from datetime import datetime
from home.models import Contact 
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
      
        contact = Contact(name=name, email = email, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been submitted !!')
    return render(request,'contact.html')

def smoothies(request):
    return render(request,'smoothies.html')

def search(request):
    query= request.GET['query']
    template = Post.objects.filter(title__icontains=query)
    params = {'templates': template}
    return render(request,'search.html', params)

def maindishes(request):
    return render(request,'maindishes.html')

def tacor(request):
    return render(request,'tacor.html')

def apricotr(request):
    return render(request,'apricotr.html')

def padr(request):
    return render(request,'padr.html')

def methir(request):
    return render(request,'methir.html')

def brownr(request):
    return render(request,'brownr.html')

def falr(request):
    return render(request,'falr.html')

def sandw(request):
    return render(request,'sandw.html')

def cutlets(request):
    return render(request,'cutlets.html')

def pestop(request):
    return render(request,'pestop.html')

def calzone(request):
    return render(request,'calzone.html')