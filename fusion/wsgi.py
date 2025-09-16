"""
WSGI config for fusion project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
# Configuração dos arquivos estáticos
# dj_static -> para apresentação de arquivos estáticos.
# Cling -> é para mostrar arquivos estáticos.
# MediaCling -> é para receber (upload) arquivos de mídia.
from dj_static import Cling, MediaCling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fusion.settings")

application = Cling(MediaCling(get_wsgi_application()))
