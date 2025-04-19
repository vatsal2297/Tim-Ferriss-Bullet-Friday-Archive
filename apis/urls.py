from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TFFEmailViewSet

router = DefaultRouter()
router.register(r'emails', TFFEmailViewSet, basename = 'email')

urlpatterns = [
    path('emails/<int:year>/', TFFEmailViewSet.as_view(actions={'get': 'list'}), name='Bullet Emails by Year'),
    path('', include(router.urls)),
]

