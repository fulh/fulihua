from django.shortcuts import render

# Create your views here.
def video2(request,*args,**kwargs):
    print(args),
    for k, v in kwargs.items():
        print(k,v),
    return render(request,'video.html',)