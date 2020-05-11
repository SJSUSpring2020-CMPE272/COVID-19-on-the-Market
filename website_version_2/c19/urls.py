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

    path('buttons', views.buttons),
    path('cards', views.cards),
    path('register', views.register),
    path('forgotpassword', views.forgotpassword),

    path('404page', views.fourpage),
    path('blankpage', views.blankpage),

    path('charts', views.charts),
    path('tables', views.tables),

    path('colors', views.colors),
    path('borders', views.borders),
    path('animations', views.animations),
    path('other', views.other),

    path('receive_input_sp', views.receive_input_sp),

    path('receive_input_dj', views.receive_input_dj),

    path('receive_input_un', views.receive_input_un)



]