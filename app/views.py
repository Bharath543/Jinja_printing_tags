from django.shortcuts import render

# Create your views here.
def printing_tags(request):
    d={'a':'abc','age':22}
    return render(request,'h1.html',context=d)