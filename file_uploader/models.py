from django.db import models
from django.contrib.auth import get_user_model


class File(models.Model):
    author = models.ForeignKey(get_user_model(), related_name='files', null=False, on_delete=models.CASCADE)
    file = models.FileField(upload_to='%Y/%m/%d')
