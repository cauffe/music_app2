from django.shortcuts import render, redirect, render_to_response
from app.models import Artist, Album
from app.forms import CustomUserCreationForm, CustomUserLoginForm, CreateAlbumForm, EditAlbumForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import RequestContext

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@staff_member_required
def delete_album(request, pk):

	album = Album.objects.get(pk=pk)

	album.delete()

	artist = album.artist

	return redirect('/artist_detail/%s' % artist.pk)

@staff_member_required
def create_album(request):

	context = {}

	form = CreateAlbumForm()

	context['form'] = form

	if request.method == 'POST':
		form = CreateAlbumForm(request.POST)

		if form.is_valid():
			form.save()

		context['form'] = form

	return render_to_response('create_album.html', context, context_instance=RequestContext(request))

@staff_member_required
def edit_album(request, pk):
	context = {}

	album = Album.objects.get(pk=pk)

	context['album'] = album

	form = EditAlbumForm(request.POST or None, instance=album)

	context['form'] = form

	if form.is_valid():
		form.save()

		return redirect('/edit_album/%s/' % album.id )

	return render_to_response('edit_album.html', context, context_instance=RequestContext(request))

def login_view(request):
	context = {}

	context['form'] = CustomUserLoginForm()

	if request.method == 'POST':

		form = CustomUserLoginForm(request.POST)
		context['form'] = form

		if form.is_valid():
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password', None)

			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)
			except Exception, e:
				message = """
				username or password incorrect, try again
				<a href='/login/'>login<a>
				"""
				return HttpResponse(message)

	return render(request, 'signin.html', context)


def sign_up(request):

	context = {}

	context['form'] = CustomUserCreationForm()

	if request.method == 'POST':

		form = CustomUserCreationForm(request.POST)
		context['form'] = form

		if form.is_valid():
			form.save()
			email = form.cleaned_data.get('email', None)
			password = form.cleaned_data.get('password1', None)

			auth_user = authenticate(username=email, password=password)

			try:
				login(request, auth_user)
			except Exception, e:
				print e
				return HttpResponse('invalid user, try again <a href="/signup/">here</a>')

	return render(request, 'signup.html', context)



def logout_view(request):
	logout(request)

	return redirect('/signup/')


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

def album_list(request):
	context = {}

	albums = Album.objects.all()

	context['albums'] = albums

	return render(request, 'album_list.html', context)


def album_detail(request, pk):
	context = {}

	album = Album.objects.get(pk=pk)

	context['album'] = album
	
	return render(request, 'album_detail.html', context)





