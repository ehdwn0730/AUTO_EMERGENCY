from django.shortcuts import render
from .models import client, situation
from django.http import HttpResponseRedirect
# Create your views here.

def blog(request):
    clientlist = situation.objects.filter(progress = 2)

    result = []

    for i in clientlist:
        result.append(client.objects.filter(client_name = i.client_id)[0])

    context ={
        'clientlist' : result,
    }
    # blog.html 페이지를 열 때, 모든 Post인 postlist도 같이 가져옴
    return render(request, 'board/blog.html', context)


def rescuer(request):
    result = []

    result.append(client.objects.filter(client_id=request.GET['id'])[0])
    print(result)
    context = {
        'post' : result
    }
    return render(request, 'board/rescuer.html', context)

def finish(request):
    situation.objects.filter(progress=2).update(progress=3)
    return HttpResponseRedirect("/blog")

def video(request):
    return render(request, "board/rescuer.html")

def video(request):
    return render(request, "board/detail.html")

def control(request):
    list = situation.objects.filter(progress = 1)

    result = []

    for i in list:
        result.append(client.objects.filter(client_name=i.client_id)[0])

    context = {
        'list': result,
    }
    return render(request, "board/control.html", context)

def detail(request):
    result = []

    result.append(client.objects.filter(client_id=request.GET['id'])[0])
    print(result)
    context = {
        'post': result
    }
    return render(request, "board/detail.html", context)

def call(request):
    situation.objects.filter(progress=1).update(progress=2)
    return HttpResponseRedirect("/control")