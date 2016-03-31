from django.shortcuts import render
from app.models import Artist
# Create your views here.

def artist_list(request):
	context = {}

	artists = Artist.objects.all()

	context['artists'] = artists

	return render(request, 'artist_list.html', context)


def artist_detail(request, pk):
	context = {}

	artist = Artist.objects.get(pk=pk)

	context['artist'] = artist
	
	return render(request, 'artist_detail.html', context)
