from django.urls import path
from .views import * 


urlpatterns = [
   
    path('category',CategoryAPI.as_view()),
    path('category/<str:pk>',CategoryAPI.as_view()),
    
    path('products',ProductAPI.as_view()),
    path('products/<str:pk>',ProductAPI.as_view()),
    
    path('contact-us',ContactUsAPI.as_view()),
    path('contact-us/<str:pk>',ContactUsAPI.as_view()),
      
]