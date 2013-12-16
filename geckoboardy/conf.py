# Configuration defaults

# To set any of this manually, please create a config.py
# and reset the variables it that module.


# Enable/Disable debug
DEBUG = True

# Services to provide
SERVICES = []

# Server name (IP:PORT)
SERVER_NAME = '127.0.0.1:5000'

# Load local config -if any-
try:
    from config import *
except ImportError as e:
    pass
