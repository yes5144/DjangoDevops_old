from django.shortcuts import render,HttpResponse,redirect
from cmdb import models
# Create your views here.
def index(request):
    return HttpResponse('welcome to index')

def dashboard(request):
    print("dashboard")
    return render(request,'cmdb/dashboard.html')

def assets(request):
    print('assets')
    assets_list = models.Assets.objects.all()
    print(type(assets_list),assets_list)
    return render(request,'cmdb/assets.html',{'assets_list':assets_list})

def detail(request,nid):
    asset_info = models.Assets.objects.filter(id=nid)
    for i in asset_info:
        print(type(i),i)
    print(type(asset_info),asset_info)
    return render(request,'cmdb/detail.html',{'asset_info':asset_info})

def edit(request,nid):
    if request.method =="POST":
        print(request.POST)
        return HttpResponse('ok')
    print('edit',nid)
    asset_info = models.Assets.objects.filter(id=nid)
    print(request.GET)
    return render(request,'cmdb/edit.html',{'asset_info':asset_info})

def addhost(request):
    if request.method =="POST":
        print(request.POST)
        assets_list = models.Assets.objects.all()
        return redirect('/cmdb/assets',{'assets_list':assets_list})
    print('addhost')
    print(request.GET)
    return render(request,'cmdb/addhost.html')