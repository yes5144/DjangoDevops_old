from django.shortcuts import render,HttpResponse,HttpResponseRedirect

# Create your views here.
def index(request):
    return HttpResponse('welcome to index')

def dashboard(request):
    print("dashboard")
    return render(request,'cmdb/dashboard.html')

def detail(request):
    print('detail')
    return render(request,'cmdb/detail.html')