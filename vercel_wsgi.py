import sys
import os

# Add project path to sys.path
sys.path.append(os.path.dirname(__file__))

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inventory.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
