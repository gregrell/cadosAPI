from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocate/', views.advocate_list),
    path('advocate/<str:username>', views.advocate_detail),
]
