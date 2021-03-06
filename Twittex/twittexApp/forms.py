from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import Posts, User, UserProfile, List


class newPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['inhalt', 'hashtags', 'mentioned', 'datum']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def clean(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password != password2:
            raise forms.ValidationError("Passwords don't match")

        return self.cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(pk=self.instance.pk).filter(username=username).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Username "%s" is already in use.' % email)
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['desc', 'picture', 'privacy']

class PostsName(object):
    model = Posts

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Posts'})
        return kwargs

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['title', 'admin']

    def clean_title(self):
        title = self.cleaned_data['title']
        if List.objects.exclude(pk=self.instance.pk).filter(title=title).exists():
            raise forms.ValidationError(u'Title "%s" is already in use.' % title)
        if title.isspace():
            raise forms.ValidationError('')
        return title
