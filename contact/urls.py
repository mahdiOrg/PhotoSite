from django.urls import path
from .views import message

app_name = 'contact'
urlpatterns = [
    path('', message, name='message')
]
