from django.utils.deprecation import MiddlewareMixin
from .models import Organization, set_current_organization

class OrganizationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        org_id = request.headers.get("X-Org-Id") or request.META.get("HTTP_X_ORG_ID")
        request.organization = None
        if org_id:
            try:
                org = Organization.objects.get(pk=int(org_id))
                request.organization = org
                set_current_organization(org)
            except (Organization.DoesNotExist, ValueError):
                pass

    def process_response(self, request, response):
        set_current_organization(None)
        return response
