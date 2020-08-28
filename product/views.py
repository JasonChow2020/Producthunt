from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required # only for logged in user
from .models import product
from django.utils import timezone

def home(request):
    Product = product.objects
    return render(request, 'product/home.html', {'product': Product})

@login_required(login_url="/account/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            Product = product() #induce class product
            Product.title = request.POST['title'] # object.xxx = input value
            Product.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                Product.url = request.POST['url']
            else:
                Product.url = 'http://' + request.POST['url']
            Product.icon = request.FILES['icon'] #image = FILES
            Product.image = request.FILES['image']
            Product.pub_date = timezone.datetime.now()
            Product.hunter = request.user ##imported in models
            Product.save() #saved and given id
            return redirect('/product/' + str(Product.id)) #it will jump to product urls.py
        else:
            return render(request, 'product/create.html', {'error': 'All fields must be filled'})
    else:
        return render(request, 'product/create.html')

def detail(request, product_id): #urls.py pass request to here
    Product = get_object_or_404(product, pk=product_id)
    return render(request, 'product/detail.html', {'product': Product})

@login_required(login_url="/account/signup")
def upvote(request, product_id):
    if request.method == 'POST':
        Product = get_object_or_404(product, pk=product_id)
        Product.vote_total += 1
        Product.save()
        return redirect('/product/' + str(Product.id))