"""
WSGI config for ccc_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
from whitenoise import WhiteNoise

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ccc_backend.settings')

wsgiApp = get_wsgi_application()

application = WhiteNoise(wsgiApp, root="/path/to/static/files")
application.add_files("/path/to/more/static/files", prefix="more-files/")
