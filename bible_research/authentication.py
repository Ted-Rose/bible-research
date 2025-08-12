"""
Custom authentication classes for the Bible Research project.
"""
from rest_framework.authentication import TokenAuthentication, SessionAuthentication


class BearerTokenAuthentication(TokenAuthentication):
    """
    Simple token based authentication using the keyword 'Bearer' instead of 'Token'.

    Clients should authenticate by passing the token key in the "Authorization"
    HTTP header, prepended with the string "Bearer ".  For example:

        Authorization: Bearer 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b
    """
    keyword = 'Bearer'


class CSRFExemptSessionAuthentication(SessionAuthentication):
    """
    Session authentication that does not enforce CSRF validation.

    This is useful for API endpoints that are accessed by a separate frontend
    application where CSRF tokens are not easily available.

    WARNING: This reduces security and should only be used when necessary.
    """

    def enforce_csrf(self, request):
        # Do not enforce CSRF validation
        return
