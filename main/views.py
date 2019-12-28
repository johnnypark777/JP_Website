from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_view(request,*args,**kwargs):
    print(request.user)
    #return HttpResponse("<h1>Test website please ignore </h1>");
    return render(request,"home.html",{})

def bigshaq(request,*args,**kwargs):
    print(request.user)
    return render(request,"bigshaq.html",{})

def about_view(request,*args,**kwargs):
    test_1 = {
            "Title":"testing Django built-in templates tags and filters",
            "text_1":"test",
            "number_1":"42069",
            "list_1":[420,42069,69]
        }
    print(request.user)
    return render(request,"about.html",test_1)

def projects_view(request,*args,**kwargs):
    print(request.user)
    return render(request,"projects.html",{})
