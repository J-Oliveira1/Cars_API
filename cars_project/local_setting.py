# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-e@@i(sysp3j8ivyjbyiqn^d*88swa21lz%y5j!&=xpy&d9-5=h'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}