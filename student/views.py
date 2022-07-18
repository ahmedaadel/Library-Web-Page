from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.
def search(request):
    search = Book.objects.all()
    title = None
    if 'searchName' in request.GET:
        title = request.GET['searchName']
        if title:
            search = search.filter(title__icontains=title)
    context ={
        'books' : search,
    }
    return render(request,'m7m.html',context)

def update(request):
    return render(request,'h1.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request, 'login.html')
    
def index(request):
    return render(request, 'indexx.html')

def add(request):
    contex ={
        'form' : BookForm()
    }
    return render(request, 'index2.html',contex)

def remove(request):
    title = request.POST.get('title')
    
    if title is not None:
        book = Book.objects.get(title=title)
        book.delete()
    return render(request,'deleteBook.html')