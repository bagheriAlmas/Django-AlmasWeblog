from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def user_register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.avatar = form.cleaned_data.get('avatar')
            user.save()
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
