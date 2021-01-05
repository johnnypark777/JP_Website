from django.shortcuts import render, redirect

# Create your views here.
from main.forms import FileForm
from main.models import File


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


def file_list(request):
    books = File.objects.all()
    return render(request, 'file_list.html', {
        'files': books
    })


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')
