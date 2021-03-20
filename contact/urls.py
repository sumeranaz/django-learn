from django.urls import path

from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('hello/', views.say_hello, name='say_hello'),
    # path('contents', views.contents, name='contens'),
    # path('sami/', views.index2, name='index2'),
    # path('Faro/', views.index3, name='index3'),
    # path('index/', views.index, name='index'),
]