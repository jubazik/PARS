from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import UploadFileView, idexs

urlpatterns = [
    path('', idexs, name='hom'),
    path('upload/', UploadFileView.as_view(), name='upload_file')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
