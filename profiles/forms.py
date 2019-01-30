from django import forms

from .models import Profile


class ProfileForm(forms.ModelForm):
    """Форма профиля"""

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'company_name',
            'country',
            'state',
            'city',
            'address',
            'postcode',
            'phone')