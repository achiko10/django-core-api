# core/models.py (სწორი და სრული ვერსია)

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # როლის კონსტანტები
    MANAGER = 1
    INSPECTOR = 2
    CLIENT = 3
    
    ROLE_CHOICES = (
        (MANAGER, 'Manager'),
        (INSPECTOR, 'Inspector'),
        (CLIENT, 'Client'),
    )
    
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=INSPECTOR)
    
    REQUIRED_FIELDS = ['role', 'first_name', 'last_name', 'email']
    
    # --- related_name კონფლიქტის მოგვარება ---
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set', # უნიკალური სახელი
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions_set', # უნიკალური სახელი
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    # ----------------------------------------

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

class Company(models.Model):
    name = models.CharField(max_length=255)
    client_contact = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, # ეს აუცილებელია Admin-ში ცარიელი ველის დასაშვებად
        limit_choices_to={'role': User.CLIENT}, 
        related_name='client_companies'
    )
    
    def __str__(self):
        return self.name

class Site(models.Model): # დარწმუნდით, რომ ეს მოდელი არსებობს!
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='sites')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return f"{self.name} ({self.company.name})"