from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def user_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            username = form['username']
            print(username)
            user = form.save(commit=False)
            user.avatar = form.cleaned_data.get('avatar')
            user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_detail_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user_articles = user.Articles.all()
    return render(request, 'users/user_profile.html', {'user': user, 'articles': user_articles})


def user_update_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user_articles = user.Articles.all()
    return render(request, 'users/user_update.html', {'user': user, 'articles': user_articles})


# def user_update_view(request,pk):
#
#     if request.method == 'POST':
#         form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = CustomUserChangeForm(instance=request.user)
#
#     return render(request, 'users/user_update.html', {'form': form})
