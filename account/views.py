from django.shortcuts import render,render_to_response, redirect, get_object_or_404
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm, ObservationForm
from .models import Profile
from board.models import Image
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):

    return render(request, 'account/index.html')

def register(request):

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user)

            auth_login(request, user)

            return redirect('/account/profile/')

    else:
        form = UserRegistrationForm()

    return render(request, 'account/register.html', {'form': form})

@login_required(login_url='account/login/')
def profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return render(request, 'account/upload_success.html', {'message': 'Upload Success!'})
    else:
        form = ProfileForm()

    return render(request, 'account/upload.html', {'form': form})

def login(request):

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request,user)

                return render(request, 'account/login_success.html', {'user': user})
    else:
        form = UserLoginForm()

    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return render(request, 'account/logout.html', {'message': 'You have been logged out successfully!'})


def delete_avatar(request):

    user = get_object_or_404(User, username=request.user)
    user.profile.avatar.delete()

    return render(request, 'account/avatar_deleted.html',{'message': 'Avatar Deleted!'})

def search_for_user(request):

    if request.method == 'POST':
        form = ObservationForm(request.POST)
        searched_user = request.POST['search_user']
        try:
            user_query = User.objects.get(username=searched_user)
        except User.DoesNotExist:
            return render_to_response('account/user_not_found.html')

        if form.is_valid():
            form.save(commit=False)
            form.instance.subject = request.user
            form.instance.target = user_query
            form.save()
            return render(request,'account/user_added.html',{'message': 'user added!'})

    else:
        form = ObservationForm()

    return render(request, 'account/search_user.html', {'form': form})