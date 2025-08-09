import re
from django.conf import settings
from django.http import HttpResponseForbidden


class RegexHostMiddleware:
    """
    Middleware that validates requests against regex patterns in
    ALLOWED_HOST_REGEXES.

    Similar to how CORS_ALLOWED_ORIGIN_REGEXES works, but for host validation.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # Compile regex patterns at initialization time for better performance
        self.allowed_host_regexes = []
        if hasattr(settings, 'ALLOWED_HOST_REGEXES'):
            for pattern in settings.ALLOWED_HOST_REGEXES:
                self.allowed_host_regexes.append(re.compile(pattern))

    def __call__(self, request):
        host = request.get_host()

        # First check if the host is in the standard ALLOWED_HOSTS
        if host in settings.ALLOWED_HOSTS:
            return self.get_response(request)

        # Then check against regex patterns
        for regex in self.allowed_host_regexes:
            if regex.match(host):
                return self.get_response(request)

        # If we get here, the host is not allowed
        return HttpResponseForbidden(f"Invalid host header: {host}")
