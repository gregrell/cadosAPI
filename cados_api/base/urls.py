from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)



urlpatterns = [
    # next 2 lines are import from djangorestframework API authentication
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.endpoints),
    path('advocate/', views.advocate_list, name='advocates'),
    path('advocate/<str:username>', views.advocate_detail),
    path('company/', views.companies_list),
]
