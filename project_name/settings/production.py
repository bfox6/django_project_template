from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    # 'project_name.crc.nd.edu',
    # 'project_name.crc.virtual.nd.edu',
]

# Load optional settings specific to the local system (for example, custom settings on a developer's system).
# The file "local.py" is excluded from version control.
try:
    from .local import *
except ImportError:
    pass
