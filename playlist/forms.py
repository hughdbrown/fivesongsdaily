import logging

from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from fivesongsdaily.playlist.models import Song, Playlist, Comment

class CommentForm(ModelForm):
    fullname = forms.CharField(label='Your Name', error_messages={'required': 'Please enter your name.'})
    email = forms.CharField(label='Your Email Address', error_messages={'required': 'Please enter a valid email address.'})
    website = forms.URLField(label='Your Web Site', required=False)
    body = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Please enter a comment.'})

    class Meta:
        model = Comment

class SongForm(ModelForm):
    artist = forms.CharField(label='Artist:', widget=forms.TextInput(attrs={' class': 'input_short' }), required=True)
    title = forms.CharField(label='Title:', widget=forms.TextInput(attrs={' class': 'input_short' }), required=True)
    filepath = forms.FileField(label='File:', required=True)

    class Meta:
        model = Song
        exclude = ('user',)

class PlaylistForm(ModelForm):
    def clean(self): 
        data = dict((k, v) for k,v in self.cleaned_data.iteritems() if (type(v) is str or type(v) is unicode))
        logging.debug('CLEANED DATA ================ %s' %data)
        names = [("song" + str(i)) for i in range(1, 6)]
        s = set(self.cleaned_data[name] for name in names)
        if len(s) != len(names) :
            raise forms.ValidationError(_(u'You have selected the same song more than once - try again.'))
        return self.cleaned_data

    class Meta:
        model = Playlist
        exclude = ('user',)

