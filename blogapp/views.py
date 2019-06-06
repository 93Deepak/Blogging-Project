from django.shortcuts import render
from blogapp.forms import UserForm
from blogapp.forms import BlogForm
from blogapp.models import Blogs
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
def index(request):
    return render(request,'blogapp/index.html')

@login_required
def postblog(request):
    if request.method=='POST':
        img=BlogForm(request.POST, request.FILES)
        if img.is_valid():
            data=img.save(commit=False)
            data.author=request.user
            data.save()
            return HttpResponseRedirect(reverse('post'))
    else:
        img=BlogForm()
        images=Blogs.objects.all().order_by('upload_date')
        return render (request,'blogapp/postblog.html',{'form':img,'images':images})

def viewblog(request):
    bloglist=Blogs.objects.all()
    mydict={'bloglist':bloglist}
    return render(request,'blogapp/viewblog.html', context=mydict)

def signup(request):
    form=UserForm()
    mydict={'userform':form}
    if request.method=='GET':
        form=UserForm(request.GET)
        form.save()
        print('data inserted in DB successfully..')
    return render(request,'blogapp/signup.html',context=mydict)

def login(request):
    return render(request,'blogapp/login.html')
