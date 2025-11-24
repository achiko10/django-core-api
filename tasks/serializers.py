# tasks/serializers.py
from rest_framework import serializers
from .models import Task, TaskMedia

class TaskSerializer(serializers.ModelSerializer):
    site_name = serializers.CharField(source='site.name', read_only=True)
    company_name = serializers.CharField(source='site.company.name', read_only=True)
    
    class Meta:
        model = Task
        # დავამატეთ id (რაც Pylance-მა ვერ დაინახა)
        fields = ('id', 'title', 'description', 'status', 'site_name', 'company_name', 'planned_due_date')

class TaskMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskMedia
        fields = ('id', 'file', 'comment', 'uploaded_by', 'uploaded_at')

class TaskDetailSerializer(TaskSerializer):
    media = TaskMediaSerializer(many=True, read_only=True)
    
    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ('media',)