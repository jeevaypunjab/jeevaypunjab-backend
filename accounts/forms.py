from django import forms

from .models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('profile_photo', 'phone_number', 'about', 'facebook',
                  'instagram')

    def clean_phone_number(self):
        if not self.cleaned_data.get('phone_number'):
            return None
        return self.cleaned_data.get('phone_number')

    def clean_facebook(self):
        if not self.cleaned_data.get('facebook'):
            return None
        return self.cleaned_data.get('facebook')

    def clean_instagram(self):
        if not self.cleaned_data.get('instagram'):
            return None
        return self.cleaned_data.get('instagram')
