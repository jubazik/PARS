import os
from documents.g_2b import *
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.views.generic import ListView
from .models import Document, Cargo


class UploadFileView(View):
    def get(self, request):
        return render(request, "gu_2b/downloads.html")

    def post(self, request):
        try:
            uploaded_file = request.FILES.get('file')
            if uploaded_file:
                file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)

                # Сохраняем файл
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)

                # Парсим файл
                parser = HTMLParser(file_path)
                parser.parse()
                data = parser.get_data()

                # Сохраняем данные в базу
                document = Document.objects.create(
                    number=data['number'],
                    station=data['station'],
                    notification=data['notification'],
                    date=data['date'],
                    client_name=data['client_name'],
                    place_of_transfer=data['place_of_transfer'],
                    locomotive=data['locomotive'],
                    route_belonging=data['route_belonging'],
                    client_representative=data['client_representative']
                )

                for item in data['table_data']:
                    Cargo.objects.create(
                        document=document,
                        wagon=item['wagon'],
                        container_and_size=item['container_and_size'],
                        type=item['type'],
                        control_mark=item['control_mark'],
                        operation=item['operation'],
                        cargo_names=item['cargo_names'],
                        note=item['note']
                    )

                # Удаляем файл
                os.remove(file_path)

                return JsonResponse({'status': 'success', 'message': 'File processed and data saved.'})
        except:
            return JsonResponse({'status': 'error', 'message': 'No file uploaded.'})


# class DocumentCargo(ListView):
#     model = Document
#     templates_name = 'gu_2b/index.html'
#     context_object_name = "document"
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         document = [doc for doc in Document.objects.all()]
#         return document

def idexs(request):
    context = "Главная"
    documents = Document.objects.all()

    return render(request, "gu_2b/index.html", {"documents": documents, "title": context})

# Create your views here.
