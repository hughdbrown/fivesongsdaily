from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from fivesongsdaily.profiles.models import UserProfile
from fivesongsdaily.profiles.data.choices import states, countries

class UserProfileForm(ModelForm):
    state = forms.ChoiceField(label='State', widget=forms.Select(attrs={'class':'input_select'}), choices=states, required=False)
    country = forms.ChoiceField(label='Country', widget=forms.Select(attrs={'class':'input_select'}), choices=countries, required=False)
    favorite_bands = forms.CharField(label='Favorite bands (comma-separated)', widget=forms.widgets.Textarea(), required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)



