from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from .models import Features
def index(request):
    '''context ={
        'name': 'Pattrick', 
        'age': 13, 
        'nationality':'British'
    }
    return render(request,'index.html', context)'''
    '''
    feature1 = Features()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our service is very quick'
    '''
    features = Features.objects.all()
    return render(request, 'index.html', {'features': features})

# For User sign up and authentication
from django.contrib.auth.models import User, auth  
from django.contrib import messages                                         
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        reppass = request.POST['reppass']

        if password == reppass: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('register.html')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login.html')
        else:
            messages.info(request, 'Passwords are not the same!')
            return redirect('register.html')
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None: 
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login.html')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split(' '))
    return render(request,'counter.html', {'amount': amount_of_words})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})