from django.urls import path, include
from users.views import UserApiView, RegisterApiView, UserDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('drf/v1/auth/', include('rest_framework.urls')),
    path('userlist/', UserApiView.as_view()),
    path('userdetail/<int:pk>', UserDetail.as_view()),
    path('registerapi/', RegisterApiView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]