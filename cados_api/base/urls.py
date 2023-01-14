from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocate/', views.advocate_list, name='advocates'),
    path('advocate/<str:username>', views.advocate_detail),
    path('company/', views.companies_list),
]
