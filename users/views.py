import json
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from users.forms import ProfileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from review.models import Review
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.core import serializers
from users.models import Profile
from book.models import Book
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def profile(request):
    profile_form = ProfileUpdateForm(instance=request.user.profile)

    if request.method == 'POST':
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    context = {
        'username': request.user.username,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)

def get_user_review(request):
    user_review = Review.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', user_review))

def show_user_review(request):
    return render(request, 'user_review.html')

def show_profile_json (request):
    data = Profile.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data))

@csrf_exempt
def update_profile_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        profile = Profile.objects.get(user=request.user)
        
        profile.email = data["email"]
        profile.first_name = data["first_name"]
        profile.last_name = data["last_name"]
        profile.address = data["address"]
        profile.phone_number = data["phone_number"]
        profile.gender = data["gender"]
        profile.save()

        return JsonResponse({"status": "success"}, status=200)

    else:
        return JsonResponse({"status": "error"}, status=401)





