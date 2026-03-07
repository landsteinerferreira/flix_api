import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^*y=nxuw#_x60j7oxebfh^gmy!h892xh^j+#t2p*3391=4kc=q"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #"unfold",
    "jazzmin",  # Deve vir primeiro!
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",

    "genres",
    "actors",
    "movies",
    "reviews",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'

# Para pegar a logo temos que direcionar essa pasta
STATICFILES_DIRS = [
    BASE_DIR / "app" / "static",
]


JAZZMIN_SETTINGS = {
    "site_logo": "logo.png",
    "site_title": "Flix API",
    "site_icon": "logo.png",  # Esta linha adiciona a logo na aba do navegador
    # Logo para dispositivos móveis (opcional)
    "site_logo_mobile": None,
    "site_header": "Painel de Controle",
    "site_brand": " ",
    "welcome_sign": "Bem-vindo ao sistema",
    # "copyright": "L11 Web - By Landsteiner Ferreira",
    # "show_sidebar": True,
    # "navigation_expanded": True,


    # Se você quiser esconder uma aplicação inteira (como 'auth' ou 'admin')
    "hide_apps": ["auth"], 

    # Se quiser esconder modelos específicos
    "hide_models": ["auth.user", "auth.group"],
    
    
# Menu Suspenso
    "topmenu_links": [

        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"app": "genres"},
        {"app": "actors"},
        {"app": "movies"},
    ],
    

    

}


JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    #"theme": "simplex",
    "custom_css": "static/css/custom_admin.css", 
}
