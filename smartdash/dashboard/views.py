import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Quote


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'landing.html')

def utilities_page(request):
    return render(request, 'utilities.html')

@login_required
def random_quote(request):
    quotes = Quote.objects.all()
    quote = random.choice(quotes) if quotes else None
    return render(request, 'quotes.html', {'quote': quote})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me', False) == 'on'
        
        user = authenticate(request, username=username, password=password)
        if user:
            if remember_me:
                request.session.set_expiry(60 * 60 * 24 * 30)
            else:
                request.session.set_expiry(0)
                
            login(request, user)
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                login(request, user)
                return redirect('/dashboard')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'signup.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout.html')

@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')

@login_required
def profile_view(request):
    return render(request, 'profile.html')

@login_required
def calculator_view(request):
    return render(request, 'calculator.html')

@login_required
def notepad_view(request):
    return render(request, 'notepad.html')
@login_required
def unit_converter_view(request):
    return render(request, 'unit_converter.html')

@login_required
def currency_converter_view(request):
    return render(request, 'currency_converter.html')

@login_required
def calendar_view(request):
    return render(request, 'calender.html')

@login_required
@ensure_csrf_cookie
def weather_view(request):
    return render(request, 'weather.html')

@login_required
def clock_view(request):
    return render(request, 'clock.html')