"""
WSGI config for Django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/root/.pyenv/versions/3.5.3/lib/python3.5/site-packages')
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(path)
if path not in sys.path:
    sys.path.append(path)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

application = get_wsgi_application()
