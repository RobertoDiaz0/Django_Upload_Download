from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import mimetypes
nombre_del_archivo = None

# Create your views here.
def UploadView(request):

    if request.method == 'GET':
        return render(request, 'Upload.html')
    elif request.method == 'POST':
        archivo = request.FILES['upload'] #upload viene de la propiedad name del TEMPLATE
        archivo_guardado = FileSystemStorage().save(archivo.name, archivo)
        global nombre_del_archivo
        nombre_del_archivo = str(archivo.name)
        return render(request, 'Download.html')

def DownloadView(request):
    archivo_path = settings.MEDIA_ROOT + "/" + nombre_del_archivo
    archivo = open(archivo_path, 'rb')
    type = mimetypes.guess_type(archivo_path)
    response = HttpResponse(archivo, content_type=type)
    response['Content-Disposition'] = "attachment; filename="+nombre_del_archivo
    return response
