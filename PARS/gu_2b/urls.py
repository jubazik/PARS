from django.urls import path
from .views import UploadFileView, DocumentCargo


urlpatterns = [
    path('', DocumentCargo.as_view(), name='Documents')
]
