from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterFrom(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    def __init__(self, *args, **kwargs):
        super(UserRegisterFrom, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['email'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['password1'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['password2'].widget.attrs['class'] = 'mdc-text-field__input'


class DateInput(forms.DateInput):
    input_type = 'date'

class CreateProfileForm(forms.ModelForm):

    class Meta:
        model= Profile
        fields= '__all__'
        widgets = {
            'date_of_birth': DateInput()
            }
    def __init__(self, *args, **kwargs):
        super(CreateProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['last_name'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['date_of_birth'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['phone'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['gender'].widget.attrs['class'] = 'mdc-text-field__input'
        self.fields['image'].widget.attrs['class'] = 'mdc-text-field__input'

