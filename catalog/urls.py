from django.urls import path
from .views import ProductView


urlpatterns = [
    # path('brandapi/', BrandAPIView.as_view()),
    # path('brand/<int:pk>/', )
    # path('sizeapi/', SizeView.as_view()),
    # path('categoryapi/', CategoryView.as_view()),
    path('productapi/', ProductView.as_view()),
]