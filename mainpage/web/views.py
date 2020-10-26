from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})
def archive(request):
    return render(request, 'archive.html', {})
def contact(request):
    return render(request, 'contact.html', {})
def single(request):
    return render(request, 'single.html', {})
def world(request):
    return render(request, 'world.html', {})
def korea(request):
    return render(request, 'korea.html', {})
def account(request):
    return render(request, 'account.html', {})

# Create your views here.
