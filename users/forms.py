from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from catalog.forms import StyleForfMixin
from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserForm(StyleForfMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'password', 'phone', 'country', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()