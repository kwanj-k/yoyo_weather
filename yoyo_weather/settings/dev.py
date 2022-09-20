"""
Configure development environment.
"""

from .base import *

CORS_ORIGIN_ALLOW_ALL = True
CSRF_COOKIE_SECURE = False
ALLOWED_HOSTS = ["*"]