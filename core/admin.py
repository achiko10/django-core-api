# core/admin.py
from django.contrib import admin
from .models import User, Company, Site

# დარეგისტრირება:
admin.site.register(User)
admin.site.register(Company)
admin.site.register(Site)