from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')

# CONFIGURACION CKEDITOR
CKEDITOR_UPLOAD_PATH = 'uploads/'
# quien administra las imagenes
CKEDITOR_IMAGE_BACKEND = 'pillow'
# ckeditor trabaja con jquery por eso debemos tener el cdn de jquery
CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js'
# Configurar ckeditor
CKEDITOR_CONFIGS  =  { 
    'default' :  { 
        'toolbar' :  'Custom' , 
        'toolbar_Custom' :  [ 
            [ 'Bold' ,  'Italic' ,  'Underline' ], 
            [ 'NumberedList' ,  'BulletedList' ,  '-' ,  'Outdent ' ,  ' Sangría ' ,  ' - ' ,  ' JustifyLeft ' ,  ' JustifyCenter ' ,  ' JustifyRight ' ,  ' JustifyBlock ' ], 
            [ 'Enlace ' ,  ' Desvincular ' ], 
            ['RemoveFormat' ,  'Fuente' ],
            ['Styles', 'Format', 'Font', 'FontSize'],
            [ 'TextColor' ,  'BGColor' ],
            [ 'Image'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']
        ] 
    } 
}

# {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
# EMAIL SETTINGS
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = get_secret('EMAIL')
# EMAIL_HOST_PASSWORD = get_secret('PASS_EMAIL')
# EMAIL_PORT = 587