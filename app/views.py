from django.shortcuts import render

# Create your views here.
def userdefinedfilter(request):
    d={'data':'hOW ArE YoU'}
    return render(request,'userdefinedfilter.html',d)