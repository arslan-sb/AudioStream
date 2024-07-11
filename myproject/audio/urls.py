from django.urls import path
from .views import login_view, logout_view, audio_list

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('', index, name='index'),
    path('', audio_list, name='audio_list'),
]
