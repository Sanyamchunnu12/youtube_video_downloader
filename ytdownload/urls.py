from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name =  'home'),
    path("linksubmit",views.submit, name ="submit"),
    path("<str:pixel>",views.download, name = "download"),
    path("",views.final, name = "final"),
]