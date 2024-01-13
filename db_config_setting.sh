    'default':
        {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': '127.0.0.1',
            'PORT': 5440

        }

	STATIC_URL = "static/"
MEDIA_URL = "media/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]
MEDIA_ROOT = [BASE_DIR / "media"]
#------------------------------------
#url---------------------------------
from django.conf.urls.static import static
from django.conf import settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#------------------------------
#Django Debug Toolbar
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        # ...
    }
]

INSTALLED_APPS = [
    # ...
    "debug_toolbar",
    # ...
]

#Add the URLs
from django.urls import include, path

urlpatterns = [
    # ...
    path("__debug__/", include("debug_toolbar.urls")),
]

#  Add the Middleware
MIDDLEWARE = [
    # ...
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]

#
# Configure Internal IPs
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

