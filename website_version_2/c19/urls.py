from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('form', views.form),
    path('prediction_sp', views.prediction_sp),
    path('receive_csv', views.receive_csv)
]