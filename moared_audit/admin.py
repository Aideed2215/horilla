"""
admin.py
"""

from django.contrib import admin

from moared_audit.models import AuditTag, moaredAuditInfo, moaredAuditLog

# Register your models here.

admin.site.register(AuditTag)
