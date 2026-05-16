from django.urls import path
from . import views
from .views import contact_view

app_name = 'metime'

urlpatterns = [
    path('', views.home, name='home'),
    path("contact/", contact_view, name="contact"),
    path("agrocleverland/",views.agrocleverland,name="agrocleverland"),
    path('almar/',views.almar,name='almar'),
    path('lamolebar/',views.lamolebar,name='lamolebar'),
    path('edisales/',views.edisales,name='edisales'),
    path('dataspace/',views.dataspace,name='dataspace'),
]


