import os
import sys

import django

from .settings import BASE_DIR


# WORKAROUND for resolve all inside `fw_django` by simple names
sys.path.append(BASE_DIR.as_posix())

# WORKAROUND for `django.core.exceptions.ImproperlyConfigured`
# Description:
#   You must either define the environment variable DJANGO_SETTINGS_MODULE
#   or call settings.configure() before accessing settings.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# WORKAROUND for `django.core.exceptions.AppRegistryNotReady`
# Description:
#   Apps aren't loaded yet.
django.setup(set_prefix=False)
