from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage 
from django.db.models import Q
from .forms import Regform
from .models import Form
# Create your views here.


def reg(request):
    if request.method == 'POST':
        form = Regform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view') 
    else:
        form = Regform()  
        
    return render(request,'registerapp/reg.html',{'forms':form})   

def view(request):
    blog_search = request.GET.get('search')
    if blog_search:
        posts = Form.objects.filter(Q(first_name__icontains = blog_search)|Q(last_name__icontains = blog_search))
    else:
        posts=Form.objects.all().order_by('-first_name')  
    pages = Paginator(posts,2)
    posts=pages.page(1) 
    getpage=request.GET.get('page') 
    # posts=pages.page(getpage)                                                  
    try:
        posts=pages.page(getpage)
    except PageNotAnInteger:
        posts=pages.page(1)      
    except EmptyPage:
         posts = pages.page(pages.num_pages)  
    return render(request,'registerapp/view.html',{'posts':posts,'pages':pages})     