from os import getenv

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin


class Config:
    SECRET_KEY = getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = getenv("SQLALCHEMY_TRACK_MODIFICATION")
    SECURITY_PASSWORD_SALT = getenv("SECURITY_PASSWORD_SALT")
    SECURITY_PASSWORD_HASH = getenv("SECURITY_PASSWORD_HASH")
    CELERY_BROKER_URL = 'redis://redis:6379/0'
    CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
    REDIS_URL = 'redis://redis:6379/0'
    UPLOADED_IMAGES_DEST = 'uploads/images'
    APISPEC_SPEC = APISpec(
        title='OSI',
        version='v1',
        openapi_version='2.0',
        plugins=[MarshmallowPlugin()]
    )
