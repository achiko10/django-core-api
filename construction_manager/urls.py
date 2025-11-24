# construction_manager/urls.py (ეს უნდა იყოს მთლიანი შინაარსი)

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from core.views import UserProfileViewSet
from tasks.views import AssignedTaskViewSet, TaskMediaUploadView

# Default Router-ის ინსტანცირება
router = DefaultRouter()
router.register(r'profile', UserProfileViewSet, basename='profile')
router.register(r'tasks', AssignedTaskViewSet, basename='assigned-tasks')
router.register(r'tasks/media', TaskMediaUploadView, basename='task-media-upload')


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API ენდპოინტები (ეს ხაზი აკლია!)
    path('api/', include(router.urls)), 
    
    # JWT Auth ენდპოინტები
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# დარწმუნდით, რომ არ გაქვთ ძველი urlpatterns სია სადმე ფაილის ზემოთ!