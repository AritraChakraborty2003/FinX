from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="index"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('signUpConsumer',views.signupConsumer,name="signupconsumer"),
    path('loginConsumer',views.loginConsumer,name="login"),
    path('Payment',views.payment,name="Payment"),
    path('Loan',views.Loan,name="Payment"),
    path("logout",views.logout,name="dash1"),
]