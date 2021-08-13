from django.contrib.auth.forms import UserCreationForm, forms, AuthenticationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    """ Register user form for the registration view """
    username = forms.CharField(label='Логин-имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    """ Login user form for the login view"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ImportCSVForm(forms.Form):
    """ Form for import .csv file data to the DB"""
    csv = forms.FileField(label='Файл с данными', widget=forms.FileInput(attrs={
        'accept': '.csv', 'class': 'form-control'
    }), required=True)

    class Meta:
        fields = ('csv',)


# class BedroomsForm(forms.ModelForm):
#     """ Bedroom Creation form """
#     class Meta:
#         model = Bedroom
#         fields = ['keywords']
