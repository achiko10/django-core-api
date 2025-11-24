# core/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer

class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to view their own profile (used after login).
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # მხოლოდ მიმდინარე მომხმარებლის დაბრუნება
        return User.objects.filter(id=self.request.user.id)