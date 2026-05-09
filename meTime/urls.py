from django.urls import path
from . import views
from .views import contact_view

app_name = 'meTime'

urlpatterns = [
    path('', views.home, name='home'),
    path("contact/", contact_view, name="contact"),
]

