from django.shortcuts import render, redirect
from .forms import SignUpForm, UserActivateForm
from django.core.mail import send_mail
from .models import Profile, UserAddress, UserPhoneNumber

# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data["email"]
            myform = form.save()

            profile = Profile.objects.get(user__username=username)
            profile.active = False
            profile.save()

            send_mail(
                subject="activate your account",
                message=f"use this code toactivate your account{profile.code}",
                from_email="ayoubhafidialaoui10@gmail.com",
                recipient_list=[email],
                fail_silently=False
            )
            return redirect(f"/accounts/{username}/activate")
    else:
        form = SignUpForm()
    return render(request, "registration/signUp.html", {'form': form})

def user_activate(request, username):
    profile = Profile.objects.get(user__username=username)
    if request.method == "POST":
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code  = form.cleaned_data["code"]
            if profile.code == code:
                profile.activate=True
                profile.code=""
                profile.code_used=True
                return  redirect("/accounts/login")
    else:
        form = UserActivateForm()
    return render(request, "registration/activation.html", {"form": form})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    user_address = UserAddress.objects.filter(user=request.user)
    user_phone_number = UserPhoneNumber.objects.filter(user=request.user)
    return render(request, "registration/profile.html", {"profile": profile, "user_address": user_address, "user_phone_number": user_phone_number})