from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.conf import settings
import mimetypes

def Download_View(request):
    nombre_del_archivo = "CV.pdf"
    archivo_path = settings.MEDIA_ROOT + "/" + nombre_del_archivo
    response = FileResponse(open(archivo_path, 'rb'))
    return response
