from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import mimetypes

def Download_View(request):
    nombre_del_archivo = "CV.pdf"
    archivo_path = settings.MEDIA_ROOT + "/" + nombre_del_archivo
    archivo = open(archivo_path, 'rb')
    type = mimetypes.guess_type(archivo_path)
    response = HttpResponse(archivo, content_type=type)
    response['Content-Disposition'] = "attachment; filename=CV.pdf"
    return response
