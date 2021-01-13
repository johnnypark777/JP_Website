from django.shortcuts import render, redirect
from django.http import JsonResponse, FileResponse, HttpResponseNotFound, HttpResponseRedirect 
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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


def image_list(request):
    book_json = list(File.objects.values())
    return JsonResponse(book_json, safe=False)


def image(request, pk):
    if request.method == 'GET':
        if not File.objects.filter(pk=pk).exists():
            return  HttpResponseNotFound("<h1>Error: File not found</h1>")
        tmpfile = File.objects.get(pk=pk).file
        return FileResponse(tmpfile)
    else: 
        return  HttpResponseNotFound("<h1>Page not found</h1>")


@csrf_exempt
def image_upload(request):
    print("Test")
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('https://image.johnnypark.ca')
        return HttpResponseNotFound("<h1>Error: Upload failed</h1>")
    return HttpResponseNotFound("<h1>Page not found</h1>")


@csrf_exempt
def image_delete(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")


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
