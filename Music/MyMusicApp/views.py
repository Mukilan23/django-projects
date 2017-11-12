from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Album
from django.template import loader
# Create your views here.
def index(request):
    all_albums= Album.objects.all()
    template=loader.get_template('MyMusicApp/index.html')
    context = {'all_albums':all_albums,}
    return HttpResponse(template.render(context,request))

def detail(request, album_id):
    try:
       album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
       raise Http404("Album doesnot exist")
    return render(request,'MyMusicApp/detail.html',{'album':album,})
