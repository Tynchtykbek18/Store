from django.urls import path, include
from users.views import UserApiView, RegisterApiView


urlpatterns = [
    path('drf/v1/auth/', include('rest_framework.urls')),
    path('userapi/', UserApiView.as_view()),
    path('registerapi/', RegisterApiView.as_view()),
]