from registrar.settings.base import *

DEBUG = True

# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# END CACHE CONFIGURATION

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('default.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
# END DATABASE CONFIGURATION

# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# END EMAIL CONFIGURATION

# TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
if os.environ.get('ENABLE_DJANGO_TOOLBAR', False):
    INSTALLED_APPS += (
        'debug_toolbar',
    )

    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

    DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1',)
# END TOOLBAR CONFIGURATION

# AUTHENTICATION
OAUTH2_PROVIDER_URL = 'http://edx.devstack.lms:18000/oauth2'

# Use a non-SSL URL for authorization redirects
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

# Set these to the correct values for your OAuth2/OpenID Connect provider (e.g., devstack)
SOCIAL_AUTH_EDX_OIDC_KEY = 'registrar-key'
SOCIAL_AUTH_EDX_OIDC_SECRET = 'registrar-secret'
SOCIAL_AUTH_EDX_OIDC_URL_ROOT = 'http://edx.devstack.edxapp:18000/oauth2'
SOCIAL_AUTH_EDX_OIDC_PUBLIC_URL_ROOT = 'http://localhost:18000/oauth2'
SOCIAL_AUTH_EDX_OIDC_LOGOUT_URL = 'http://localhost:18000/logout'
SOCIAL_AUTH_EDX_OIDC_ISSUER = 'http://edx.devstack.lms:18000/oauth2'
SOCIAL_AUTH_EDX_OIDC_ID_TOKEN_DECRYPTION_KEY = SOCIAL_AUTH_EDX_OIDC_SECRET

ENABLE_AUTO_AUTH = True

JWT_AUTH['JWT_ISSUERS'].append({
    'AUDIENCE': 'lms-key',
    'ISSUER': 'http://edx.devstack.lms:18000/oauth2',
    'SECRET_KEY': 'lms-secret',
})

#####################################################################
# Lastly, see if the developer has any local overrides.
if os.path.isfile(join(dirname(abspath(__file__)), 'private.py')):
    from .private import *  # pylint: disable=import-error
