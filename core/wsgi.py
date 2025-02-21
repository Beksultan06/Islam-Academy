import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")  # Используйте 'core.settings.base' вместо 'settings'

application = get_wsgi_application()
