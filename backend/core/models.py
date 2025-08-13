from django.conf import settings
from django.db import models
from tenants.models import Organization

class BaseScopedModel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="%(class)s_items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="created_%(class)s_items")
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL, related_name="updated_%(class)s_items")

    class Meta:
        abstract = True
