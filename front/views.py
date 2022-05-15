from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'pages/home.html')


def about(request):
    return render(request,'pages/about.html')

def property(request):
    return render(request,'pages/property.html')

def property_single(request,property_id):
    return render(request,'pages/property_single.html')


def agent(request):
    return render(request,'pages/agent.html')

def agent_single(request,agent_id):
    return render(request,'pages/agent_single.html')


def contact(request):
    return render(request,'pages/contact.html')