from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required # only for logged in user
from .models import product
from django.utils import timezone

def home(request):
    return render(request, 'product/home.html')

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            Product = product()
            Product.title = request.POST['title']
            Product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Product.url = request.POST['url']
            else:
                Product.url = 'http://' + request.POST['url']
            Product.icon = request.FILES['icon'] #image = FILES
            Product.image = request.FILES['image']
            Product.pub_date = timezone.datetime.now()
            Product.hunter = request.user ##imported in models
            Product.save()
            return redirect('home')
        else:
            return render(request, 'product/create.html', {'error': 'All fields must be filled'})
    else:
        return render(request, 'product/create.html')