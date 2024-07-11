# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import FileResponse, Http404
import os


#Start:: LOGIN FUNCTIONALITY
def login_view(request):
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
    # print("AAAA")
    #what is the user name?
    #step 2: navigate to folder according to username
    #st3p3: only pick and send m3u8 files
    
    parent_dir = r"D:\Music\myproject\static\arslan"
    # parent_dir = r"D:\Music\myproject\audios_to_server\arslan"
    all_audio_files = os.listdir(parent_dir)

    print(all_audio_files)
    audio_files = [audio_single for audio_single in all_audio_files if audio_single.endswith('.m3u8')]
    # audio_files = [os.path.join(parent_dir,audio_single) for audio_single in all_audio_files]
    # audio_files = AudioFile.objects.all()
    return render(request, 'testhls.html', {'audio_files': audio_files})
    # return render(request, 'index.html' )


# @login_required
# def audio_list(request):
#     parent_dir = r"D:\Music\myproject\static\arslan"
#     try:
#         all_audio_files = os.listdir(parent_dir)
#         audio_files = [audio for audio in all_audio_files if audio.endswith('.m3u8')]
#     except FileNotFoundError:
#         audio_files = []
#     return render(request, 'index2.html', {'audio_files': audio_files})

# def serve_audio(request, filename):
#     # fp=filename.split('.')[0]
#     print("aaaa", filename)
#     file_path = os.path.join(r"D:\\Music\\myproject\\static\\arslan\\", filename)
#     print("file path line 65",file_path)
#     if not os.path.exists(file_path):
#         raise Http404("File not found: " + file_path)
#         print("line 68 running")
#     content_type = 'application/vnd.apple.mpegurl' if filename.endswith('.m3u8') else 'video/mp2t'
#     print(content_type)
#     file_path=os.path.normpath(r"D:\Music\myproject\static\arslan")
#     response = FileResponse(open(file_path, 'rb'), content_type=content_type)
#     print(response)
#     response['Content-Disposition'] = 'inline; filename="%s"' % filename
    
#     return response


# from django.http import Http404, FileResponse
# import os




# def serve_audio(request, filename):
#     print("aaaa", filename)
#     file_path = os.path.join(r"D:\Music\myproject\static\arslan", filename)
#     print("file path line 65", file_path)

#     if not os.path.exists(file_path):
#         raise Http404("File not found: " + file_path)

#     # Determine content type based on the file extension
#     content_type = 'application/vnd.apple.mpegurl' if filename.endswith('.m3u8') else 'video/mp2t'
#     print(content_type)

#     try:
#         # Open the file and create the response object
#         file_path=r"D:\Music\myproject\static\arslan"
#         response = FileResponse(open(file_path, 'rb'), content_type=content_type)
#         print(response)
#         response['Content-Disposition'] = 'inline; filename="%s"' % filename
#         return response
#     except Exception as e:
#         # Log or handle any exceptions raised when opening the file
#         print("Error opening file:", e)
#         raise Http404("Error accessing file: " + str(e))


