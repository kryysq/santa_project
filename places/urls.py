from django.urls import path
from .views import home, santa_view, shuffle_santa

urlpatterns = [
    path('', home, name='home'),
    path('santa/', santa_view, name='santa'),
    path('santa/shuffle/', shuffle_santa, name='shuffle_santa'),
]