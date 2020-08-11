
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=_s!t2%y9hedq8oh5g73r%=ljj!a6c2j^&np)=(*+o+!8r9hru'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'taggit',
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'booksoft.apps.BooksoftConfig',
    'commerce.apps.CommerceConfig',
    'loyalty.apps.LoyaltyConfig',
    'marketing.apps.MarketingConfig',
    'ckeditor',
    'ckeditor_uploader',
    'workflow.apps.WorkflowConfig',
    'crm.apps.CrmConfig',
    'onlinetraining.apps.OnlinetrainingConfig',
    'customerfeedback.apps.CustomerfeedbackConfig',
    'fulstack.apps.FulstackConfig',
    'school.apps.SchoolConfig',
    'post.apps.PostConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}


ROOT_URLCONF = 'company.urls'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '/media/documents')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'home.context_processors.message_processor',
            ],
        },
    },
]

EMAIL_HOST = 'smtp.mailtrap.io'
EMAIL_HOST_USER = 'f83e5ddedca3c7'
EMAIL_HOST_PASSWORD = '7673e3d8a7edc4'
EMAIL_PORT = '2525'

WSGI_APPLICATION = 'company.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

JAZZMIN_SETTINGS = {
    # title of the window
    'site_title': 'Ehsan Software',

    # Title on the brand, and the login screen (19 chars max)
    'site_header': 'Ehsan Software',

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    #'site_logo': 'polls/img/logo.png',

    # Welcome text on the login screen
    'welcome_sign': 'Welcome to Ehsan Software',

    # Copyright on the footer
    'copyright': 'Ehsan Software Ltd',

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'auth.User',

    # Field name on user model that contains avatar image
    'user_avatar': None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

        # external url that opens in a new window (Permissions can be added)
        #{'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'polls'},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
       # {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps to base side menu ordering off of (does not need to contain all apps)
    'order_with_respect_to': ['accounts', 'polls'],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {
        'polls': [{
            'name': 'Make Messages',
            'url': 'make_messages',
            'icon': 'fa-comments',
            'permissions': ['polls.view_poll']
        }]
    },

    # Custom icons for side menu apps/models See https://www.fontawesomecheatsheet.com/font-awesome-cheatsheet-5x/
    # for a list of icon classes
    'icons': {
        'auth': 'fa-users-cog',
        'auth.user': 'fa-user',
        'auth.Group': 'fa-users',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fa-chevron-circle-right',
    'default_icon_children': 'fa-bars',

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "horizontal_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs",},
}