from django.urls import path
from .views import AboutMeView

app_name = 'about'
urlpatterns = [
    path('', AboutMeView.as_view(), name='about'),
]
