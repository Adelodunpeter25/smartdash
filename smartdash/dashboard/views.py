import random
import os
import requests
from django.conf import settings
from dotenv import load_dotenv
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.cache import cache
from .models import Quote, Note
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST, require_http_methods
from django.db.models import Q
import json

load_dotenv(os.path.join(settings.BASE_DIR, '.env'))


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

def send_welcome_email(email, username):
    api_key = os.getenv('RESEND_API_KEY')
    if api_key and api_key.startswith('"') and api_key.endswith('"'):
        api_key = api_key[1:-1]
    print(f"Resend API Key: {api_key}")  # Debug: print the API key
    url = 'https://api.resend.com/emails'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        "from": "onboarding@resend.dev",
        "to": [email],
        "subject": "Welcome to SmartDash!",
        "html": f"<h2>Welcome, {username}!</h2><p>Thank you for signing up for SmartDash. We're excited to have you on board!</p>"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Resend API Response: {response.text}")  # Debug: print the full response
        response.raise_for_status()
    except Exception as e:
        print(f"Resend API error: {e}")

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
                send_welcome_email(email, username)
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
    if request.method == 'POST':
        note_id = request.POST.get('note_id')
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if note_id:
            note = Note.objects.filter(id=note_id, user=request.user).first()
            if note:
                note.title = title
                note.content = content
                note.save()
        else:
            Note.objects.create(user=request.user, title=title, content=content)
        return redirect('notepad')
    notes = Note.objects.filter(user=request.user).order_by('-updated_at')
    return render(request, 'notepad.html', {'notes': notes})

@login_required
@require_POST
def delete_note(request, note_id):
    note = Note.objects.filter(id=note_id, user=request.user).first()
    if note:
        note.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'error': 'Note not found or not authorized.'})

# All to-do list related views and code removed

@login_required
def unit_converter_view(request):
    return render(request, 'unit_converter.html')

@login_required
def currency_converter_view(request):
    result = None
    error = None
    amount = None
    from_currency = None
    to_currency = None
    if request.method == 'POST':
        amount = request.POST.get('amount')
        from_currency = request.POST.get('from_currency')
        to_currency = request.POST.get('to_currency')
        try:
            api_key = os.getenv('CURRENCY_CONVERTER_API_KEY')
            cache_key = f"exchange_rates_{from_currency}"
            data = cache.get(cache_key)
            if not data:
                url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
                response = requests.get(url)
                data = response.json()
                cache.set(cache_key, data, timeout=3600)
            if data.get('result') == 'success' and data['conversion_rates'].get(to_currency):
                rate = data['conversion_rates'][to_currency]
                converted = float(amount) * rate
                result = f"{float(amount):,.2f} {from_currency} = {converted:,.2f} {to_currency}"
            else:
                error = f"Exchange rate for {from_currency} to {to_currency} not available."
        except Exception as e:
            error = "Error fetching exchange rate."
    return render(request, 'currency_converter.html', {
        'result': result,
        'error': error,
        'amount': amount,
        'from_currency': from_currency,
        'to_currency': to_currency,
    })

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

def stopwatch_timer_view(request):
    return render(request, 'stopwatch_timer.html')