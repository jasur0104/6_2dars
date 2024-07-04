from django.shortcuts import render
from .models import PythonBook
def home(request):
    return render(request, 'home.html')
def books(request):
    books = PythonBook.objects.all()
    return render(request, 'books.html', {'books': books})
def users(request):
    pass

# Create your views here.
