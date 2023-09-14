from django.urls import path
from apps.users.views import (
    CustomLoginView,
    CustomLogoutView,
    RegistrationView,
)

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('registration/', RegistrationView.as_view(), name='registration')
]