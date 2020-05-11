from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('form', views.form),
    path('prediction_sp', views.prediction_sp),
    path('receive_csv', views.receive_csv),
    path('graph_sp', views.graph_sp),
    path('receive_csv_dj', views.receive_csv_dj),
    path('graph_dj', views.graph_dj),
    path('prediction_dj', views.prediction_dj),
    path('prediction_un', views.prediction_un),
     path('receive_csv_un', views.receive_csv_un),
    path('graph_un', views.graph_un),


]