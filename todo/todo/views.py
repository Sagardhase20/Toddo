
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'sign.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect('todo')

    return render(request, 'sign.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            email_matches = User.objects.filter(email__iexact=username)
            if email_matches.count() == 1:
                username = email_matches.get().username

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('todo')

        messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


@login_required(login_url='login')
def todo_list(request):
    return render(request, 'todo.html')


def logout_view(request):
    logout(request)
    return redirect('login')
