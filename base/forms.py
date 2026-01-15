from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Room


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make email required
        self.fields['email'].required = True
        self.fields['name'].required = True


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'bio', 'avatar']


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
