from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from users.forms import *


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
    return render(request, 'users/user_profile.html', {'user': user})


@login_required()
def user_update_view(request, pk):
    # user = CustomUser.objects.get(pk=pk)
    user = get_object_or_404(CustomUser, pk=pk)
    form = CustomUserChangeForm(request.POST or None, instance=user)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False)

            avatar = request.FILES.get('avatar')  # Use request.FILES
            if not avatar:
                avatar = 'default_user.jpg'
            user.avatar = avatar
            user.save()
            return HttpResponseRedirect('/users/' + str(pk))
    return render(request, 'users/user_update.html', {'user': user, 'form': form})


def reporter_list_view(request):
    users = CustomUser.objects.filter(is_staff=True)
    return render(request, 'users/reporter_list.html', {'users': users})


@login_required()
def reporter_article_list_view(request, pk):
    user = CustomUser.objects.get(pk=pk)
    user_articles = user.Articles.all()
    if user.is_staff:
        return render(request, 'users/reporter_article_list.html', {'user': user, 'articles': user_articles})
