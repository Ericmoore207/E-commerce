from django.urls import path
from . import views

# URLconf
urlpatterns = [
    path('',views.say_hello)
]