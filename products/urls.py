from django.urls import path
from .views import ProductViewSet

urlpatterns =[
    path('products',ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>',ProductViewSet.as_view({
       'get': 'retrieve',
       'put': 'create',
       'delete': 'destroy' 
    }))

]