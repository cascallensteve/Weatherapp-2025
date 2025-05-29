import joblib
import numpy as np
import os
from django.http import JsonResponse
from weather_app.ml.predict import get_recommendation
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import Register  # Your custom registration form, if any
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

# from .forms import SignUpForm
def index(request):
    return render(request, 'weather/index.html')

def register_view(request):
    if request.method == "POST":
        form = Register(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after successful registration
        

        

    else:
        form = Register()

    return render(request, 'weather/register.html', {'form': form})

def profile_view(request):
    return render(request, 'weather/profile.html', {'user': request.user})


def signup_view(request):
    return render(request, 'weather/signup.html')



def home(request):
    return render(request, 'weather/home.html')

def get_weather(request):

    return render(request, 'weather/weather.html')
    
    # return render(request, 'weather/profile.html', {'user': request.user})


# Update login view to handle authentication
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            
            # Send a success message
            messages.success(request, 'Thank you for logging in!')
            
            # Redirect to the home page
            return redirect('home')  # Ensure you have a 'home' URL defined in your urls.py
        else:
            # If authentication fails, show an error message
            messages.error(request, 'Invalid username or password')
            return render(request, 'weather/login.html')
    
    # Handle GET requests: return the login page
    return render(request, 'weather/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')  # Redirect to the login page or any other page




# model training
def get_weather_data(request):
    API_KEY = "your_openweather_api_key"
    CITY = "Nairobi"
    URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

    response = requests.get(URL).json()
    
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    condition = response["weather"][0]["main"]
    wind_speed = response["wind"]["speed"]
    
    recommendation = get_recommendation(temperature, humidity, condition, wind_speed)
    
    weather_data = WeatherData.objects.create(
        temperature=temperature, humidity=humidity, weather_condition=condition,
        wind_speed=wind_speed, recommendation=recommendation
    )

    return render(request, "weather.html", {"weather_data": weather_data})



def weather_view(request):
    return render(request, 'weather/weather.html')