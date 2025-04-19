from django.urls import path, include
from TFFBullets import views

urlpatterns = [
    path('api/', include('apis.urls')),  # Include apis app's URLs
    path('', views.viewEmailData),
]