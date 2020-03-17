from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
    AWS_DEFAULT_ACL = 'public-read'


class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
