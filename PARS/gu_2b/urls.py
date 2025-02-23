from django.urls import path
from .views import UploadFileView, idexs

urlpatterns = [
    path('', idexs, name='hom'),
    path('upload/', UploadFileView.as_view(), name='upload_file')
]
