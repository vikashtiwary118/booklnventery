from django.urls import path

from .views import RegisterView,CustomAuthToken

urlpatterns = [
    path('ragister/', RegisterView.as_view()),
    path(r'api-token-auth/', CustomAuthToken.as_view())
]
