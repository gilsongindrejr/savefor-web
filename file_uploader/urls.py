from django.urls import path

from .views import UploadView

app_name = 'file_uploader'
urlpatterns = [
    path('upload', UploadView.as_view(), name='upload'),
]
