import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rental.settings')
os.environ.setdefault("DJANGO_CONFIGURATION", "BaseConfiguration")


application = get_wsgi_application()
