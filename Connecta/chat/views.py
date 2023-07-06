from django.shortcuts import render

# Create your views here.

def messege_view(request):
    return render(request,'messege.html')
