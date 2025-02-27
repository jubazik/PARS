from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from .views import UploadFileView, idexs, get_ducumen_id_carg_all

urlpatterns = [
    path('', idexs, name='hom'),
    path('gu_2b/<int:document_id>/', get_ducumen_id_carg_all, name='get_ducumen_id_carg_all'),
    path('upload/', UploadFileView.as_view(), name='upload_file')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
