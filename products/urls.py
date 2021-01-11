from django.urls import path
from .views import ProductViewSet
from .views import UserAPIView
urlpatterns =[
    path('products',ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>',ProductViewSet.as_view({
       'get': 'retrieve',
       'put': 'create',
       'delete': 'destroy' 
    })),
    path('user',UserAPIView.as_view())
]