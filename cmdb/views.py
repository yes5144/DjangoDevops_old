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
    assets_list = models.Assets.objects.filter(is_deleted=0)
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
        host_name = request.POST['host_name']
        models.Assets.objects.filter(id=nid).update(host_name=host_name)
        return HttpResponse('ok')
    print('edit',nid)
    asset_info = models.Assets.objects.filter(id=nid)
    print(request.GET)
    return render(request,'cmdb/edit.html',{'asset_info':asset_info})

def addhost(request):
    if request.method =="POST":
        host_name = request.POST['host_name']
        host_type = request.POST['host_type']
        disk_total1 = request.POST['disk_total1']
        print(host_name)
        print(host_type)
        print(disk_total1)
        new_host = models.Assets(host_name=host_name,host_type=host_type,disk_total1=disk_total1)
        new_host.save()
        # return HttpResponse('ok')
        assets_list = models.Assets.objects.filter(is_deleted=0)
        return redirect('/cmdb/assets',{'assets_list':assets_list})
    else:
        print('addhost')
        return render(request,'cmdb/addhost.html')

def delete(request,nid):
    models.Assets.objects.filter(id=nid).update(is_deleted=1)
    return HttpResponse('del ok')

import json
def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        ret = {"status":True,'error':None,'data':None}
        obj = LoginForm(request.POST)
        if obj.is_valid():
            print(obj.cleand_data)
        else:
            print(type(obj.errors))
            ret['error']=obj.errors.as_json()
            return HttpResponse(json.dumps(ret))