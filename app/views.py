from django.shortcuts import render

# Create your views here.
def asif(request):
    d={'name':'asif','mobile':7981185785}
    return render(request,'asif.html',d)