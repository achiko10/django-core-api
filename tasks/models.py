# tasks/models.py
from django.db import models
from core.models import User, Site

class Task(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'New'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]
    
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='tasks')
    # ვზღუდავთ ინსპექტორებს მხოლოდ INSPECTOR როლით
    inspector = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': User.INSPECTOR}, related_name='assigned_tasks')
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')
    
    created_at = models.DateTimeField(auto_now_add=True)
    planned_due_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Task #{self.id}: {self.title} ({self.get_status_display()})"

class TaskMedia(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='media')
    # ფაილები შეინახება 'task_media/' დირექტორიაში
    file = models.FileField(upload_to='task_media/') 
    comment = models.TextField(blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Media for Task {self.task.id}"