from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '2t6o-2nqzx0gs&ok9(0%a9h0%z=@em#i30z@2a6dm@pj30)w_x'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'django.contrib.humanize',

    # Local Apps
    'store_user.apps.StoreUserConfig',
    'store_main.apps.StoreMainConfig',
    'store_account.apps.StoreAccountConfig',
    'store_shop.apps.StoreShopConfig',
    'store_contact.apps.StoreContactConfig',
    'store_favorite.apps.StoreFavoriteConfig',
    'store_comment.apps.StoreCommentConfig',
    'store_cart.apps.StoreCartConfig',
    'store_ticket.apps.StoreTicketConfig',
    'store_setting.apps.StoreSettingConfig',
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

ROOT_URLCONF = 'Morvarid_Store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Morvarid_Store.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = 'static_root'


# Custom User Model
AUTH_USER_MODEL = 'store_user.User'

# Login Required Url
LOGIN_URL = '/'

# Send Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '**************@gmail.com'
EMAIL_HOST_PASSWORD = '**************'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Arvan Cloud Storages Settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '*******-****-****-****-*************'
AWS_SECRET_ACCESS_KEY = '********************************************************'
AWS_STORAGE_BUCKET_NAME = 'morvarid-store'
AWS_SERVICE_NAME = 'S3'
AWS_S3_ENDPOINT_URL = 'https://s3.ir-thr-at1.arvanstorage.com'
AWS_S3_FILE_OVERWRITE = False
