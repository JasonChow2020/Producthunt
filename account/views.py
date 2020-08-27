from django.shortcuts import render, redirect
from django.contrib.auth.models import User #authen
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username']) # if any of the username in database already exist
                return render(request, 'account/signup.html', {'error': 'Username already exist'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) # create new user: [username, pw)
                auth.login(request, user) # auth if user = user
                return redirect('home')

        else:
            return render(request, 'account/signup.html', {'error': 'Password does not match'})
    else:
        return render(request, 'account/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')

        else:
            return render(request, 'account/login.html', {'error': 'Username or password is incorrect'})
    else:
        return render(request, 'account/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')

    return render(request, 'account/signup.html')