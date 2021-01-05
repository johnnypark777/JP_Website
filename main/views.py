from django.shortcuts import render, redirect

# Create your views here.
from main.forms import BookForm
from main.models import Book


def home_view(request, *args, **kwargs):
    print(request.user)
    # return HttpResponse("<h1>Test website please ignore </h1>");
    return render(request, "home.html", {})


def bigshaq(request, *args, **kwargs):
    print(request.user)
    return render(request, "bigshaq.html", {})


def projects_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "projects.html", {})


def poachedegg(request, *args, **kwargs):
    print(request.user)
    return render(request, "poachedegg.html", {})


def index(request, *args, **kwargs):
    print(request.user)
    return render(request, "index.html", {})


def benson(request, *args, **kwargs):
    print(request.user)
    return render(request, "Benson.html", {})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })
