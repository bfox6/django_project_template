from .base import *

DEBUG = True

# Allow the local server and any .ngrok servers
ALLOWED_HOSTS = [
   '127.0.0.1',
   '.ngrok.io',
   'localhost',
]

# Load optional settings specific to the local system (for example, custom settings on a developer's system).
# The file "local.py" is excluded from version control.
try:
    from .local import *
except ImportError:
    pass
