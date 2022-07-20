from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
                    "title": "Home Page",
                    "content": "Bem vindo a Home Page",
              }
    return render(request, "home/home_page.html", context)
    
def about_page(request):
    context = {
                    "title": "Página Sobre about",
                    "content": "Bem vindo a página sobre"
              }
    return render(request, "about/about_page.html", context)

def contact_page(request):
    context = {
                    "title": "Página Sobre contact",
                    "content": "Bem vindo a página sobre"
              }
    return render(request, "contact/contact_page.html", context)
