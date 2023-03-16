from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'users/reporter_profile.html', {'user': user, 'articles': user_articles})


def user_update_view(request, pk):
    # user = CustomUser.objects.get(pk=pk)
    user = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserChangeForm(request.POST or None, instance=user)
    if request.method == 'POST':
        form.save()
        return HttpResponseRedirect('/users/'+ str(pk))
    # user_articles = user.Articles.all()
    return render(request, 'users/user_update.html', {'user': user, 'form': form})


def reporter_list_view(request):
    users = CustomUser.objects.filter(is_staff=True)
    return render(request, 'users/reporter_list.html', {'users': users})
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
