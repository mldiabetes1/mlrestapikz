from django.urls import path
from mlrestapi import views

urlpatterns = [
    path('',views.index_page),
    path('predict', views.predict_diabetictype),
]