# tasks/views.py
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, TaskMedia
from .serializers import TaskSerializer, TaskDetailSerializer, TaskMediaSerializer
from core.models import User

class AssignedTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Allows Inspector to see tasks assigned to them.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # მხოლოდ ინსპექტორებს შეუძლიათ თავიანთი ტასკების ნახვა
        if user.role != User.INSPECTOR:
            return Task.objects.none()
            
        return Task.objects.filter(inspector=user).order_by('planned_due_date')

class TaskMediaUploadView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Allows uploading media (photo) for a specific task.
    """
    queryset = TaskMedia.objects.all()
    serializer_class = TaskMediaSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser) # საჭიროა ფაილის ატვირთვისთვის

    def create(self, request, *args, **kwargs):
        # ამოწმებს, რომ მომხმარებელი არის ინსპექტორი
        if request.user.role != User.INSPECTOR:
            return Response({"detail": "Permission denied. Only inspectors can upload media."}, status=status.HTTP_403_FORBIDDEN)
            
        task_id = request.data.get('task')
        
        if not task_id:
             return Response({"task": "This field is required."}, status=status.HTTP_400_BAD_REQUEST)
             
        # ამოწმებს, რომ ტასკი არსებობს და მინიჭებულია ინსპექტორზე
        task = get_object_or_404(Task, id=task_id, inspector=request.user)

        # მონაცემების მომზადება TaskMediaSerializer-ისთვის
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # ინახავს TaskMedia-ს
        serializer.save(uploaded_by=request.user, task=task)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)