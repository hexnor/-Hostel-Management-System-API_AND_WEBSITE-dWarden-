from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'Hostel_Management_system.settings'
application = get_wsgi_application()
application = DjangoWhiteNoise(application)