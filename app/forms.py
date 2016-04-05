from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from app.models import CustomUser, Album

class EditAlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = '__all__'

class CreateAlbumForm(forms.ModelForm):
	added_field = forms.CharField(required=False, widget=forms.HiddenInput())

	class Meta:
		model = Album
		fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserCreationForm, self).__init__(*args, **kwargs)
		# del self.fields['username']

	class Meta:
		model = CustomUser
		fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
	def __init__(self, *args, **kwargs):
		super(CustomUserChangeForm, self).__init__(*args, **kwargs)
		del self.fields['username']

	class Meta:
		model = CustomUser
		fields = '__all__'

class CustomUserLoginForm(forms.Form):
	email = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())
