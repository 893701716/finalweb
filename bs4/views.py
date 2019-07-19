from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'bs4/index.html')


def aboutus(reuqest):
    return render(reuqest,'bs4/aboutus.html')
def menu(request):
    return render(request, 'bs4/menu.html')
def mainpage(request):
    return render(request, 'bs4/mainpage.html')
def more(request):
    return render(request, 'bs4/more.html')
def coldemo(request):
    return render(request,"coldemo.html")
def nav(request):
    return render(request,'bs4/nav.html')
def contact(request):
    return render(request,"bs4/contactus.html")
