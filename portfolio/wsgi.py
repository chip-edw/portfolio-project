"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import time
import traceback
import signal
import sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/chip/django-apps/portfolio-project')
sys.path.append('/home/chip/django-apps/portfolio-project/portfolio')
sys.path.append('/home/chip/django-apps/env/lib/python3.8/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

application = get_wsgi_application() 

