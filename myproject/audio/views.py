# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
import os


#Start:: LOGIN FUNCTIONALITY
def login_view(request):

    if request.user.is_authenticated:
        # Redirect to audio_list if the user is already logged in
        return redirect('audio_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('audio_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
    # return render(request, 'authentication/login.html', {'form': form})
#END:: LOGIN FUNCTIONALITY

#Start:: LOGout FUNCTIONALITY
def logout_view(request):
    logout(request)
    return redirect('login')
#END:: LOGOUT FUNCTIONALITY



@login_required
def audio_list(request):
    # Get the logged-in user's username
    username = request.user.username
    audio_files=[]
    # Navigate to the folder according to the username
    parent_dir = os.path.join(r"D:\Music\myproject\static", username)
    
    if os.path.exists(parent_dir):
    # List all .m3u8 files in the user's directory
        all_audio_files = os.listdir(parent_dir)
        audio_files = [audio for audio in all_audio_files if audio.endswith('.m3u8')]
    return render(request, 'testhls.html', {'audio_files': audio_files, 'username': username})