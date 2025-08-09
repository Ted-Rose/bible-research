import re
import pycountry
import requests


class DeviceAndCountryMiddleware:
    """Middleware to detect device and country information from requests.
    This middleware extracts device information from the User-Agent header
    and country information from Cloudflare headers or IP address.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process request before view is called
        self.process_device_info(request)
        self.process_country_info(request)

        # Continue processing the request
        response = self.get_response(request)
        return response

    def process_device_info(self, request):
        """Extract and log device information from the User-Agent."""
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown Device')

        android_match = re.search(
            r'Android\s+[\d\.]+;\s+([^;)]+)',
            user_agent
        )
        iphone_match = re.search(r'iPhone(?:\s+OS\s+[\d_]+)?', user_agent)
        samsung_match = re.search(r'(SM-[A-Za-z0-9]+)', user_agent)

        if android_match:
            device_model = android_match.group(1).strip()
        elif iphone_match:
            device_model = "iPhone"
        elif samsung_match:
            device_model = samsung_match.group(1)
        else:
            device_model = "Unknown"

        # Store device info in request for potential use in views
        request.device_info = {
            'model': device_model,
            'user_agent': user_agent
        }

        # Log device information
        print(f"Device model: {device_model}")
        print(f"Full user agent: {user_agent}")

    def process_country_info(self, request):
        """Extract and log country information from headers or IP."""
        country_code = request.META.get('HTTP_CF_IPCOUNTRY', 'Unknown')
        country_name = "Unknown"

        if country_code != 'Unknown':
            try:
                country_obj = pycountry.countries.get(alpha_2=country_code)
                if country_obj:
                    country_name = country_obj.name
            except (KeyError, AttributeError):
                pass
            print(f"Country: {country_name} ({country_code})")
        else:
            ip = request.META.get(
                'HTTP_X_FORWARDED_FOR',
                request.META.get('REMOTE_ADDR', '')
            )
            if ip and not (ip.startswith('192.168.') or
                           ip.startswith('10.') or
                           ip.startswith('172.')):
                try:
                    response = requests.get(
                        f'http://ip-api.com/json/{ip}',
                        timeout=2
                    )
                    if response.status_code == 200:
                        data = response.json()
                        if data.get('status') == 'success':
                            country_name = data.get('country', 'Unknown')
                            print(f"Country from IP: {country_name}")
                except (requests.RequestException, ValueError):
                    pass
            print(f"IP: {ip}")

        # Store country info in request for potential use in views
        request.country_info = {
            'code': country_code,
            'name': country_name
        }
