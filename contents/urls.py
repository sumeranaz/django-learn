from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.content, name='contents'),
    path('penchod/', views.penchod_kutta, name='penchod_kutta'),
    path('good/', views.hmmm, name='hmmm'),

]


