from django.shortcuts import render
from .forms import SignUpForm, Profile

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

            #TODO send email
    else:
        form = SignUpForm()
    return render(request, "registration/signUp.html", {'form': form})