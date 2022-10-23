from http.client import HTTPResponse
from django.shortcuts import render, HttpResponse
from blog.models import blogs
from blog.models import Contact
# Create your views here.
def blog(request):
    allblogs=blogs.objects.all()
    context={'allblogs' :allblogs }
    return render(request,'bloghome.html',context)

def blogpost(request,slug):
    req=blogs.objects.filter(slug=slug).first()
    context={'req': req}
    return render(request,'blogpost.html',context)
def addblogs(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        slug=request.POST['slug']
        shortdesc=request.POST['shortdesc']
        
        print(title,slug)
        ins=blogs(title=title,content=content,slug=slug,shortdesc=shortdesc)
        ins.save()

    return render(request,'addblogs.html')
def  contact(request): 

    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        city=request.POST['city']
        state=request.POST['state']
        zip=request.POST['zip'],

        ins= Contact(first_name=first_name,last_name=last_name,username=username,city=city,state=state,zip=zip)
        ins.save()
        print("data added to db")
    return render(request , 'contact.html')
