from django.shortcuts import render,redirect
import uuid
from .models import Url
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')


def create(request):
    if request.method=="POST":
        link=request.POST['link']
        if link=="":
            return HttpResponse("Empty")
        if Url.objects.filter(link=link).exists():
            u=Url.objects.filter(link=link).values()[0]['uuid']

            return HttpResponse(u)
        uid=str(uuid.uuid4())[:5]
        new_url=Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request,pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
