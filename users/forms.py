from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
        label='Alamat Email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'contoh@email.com'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        
        labels = {
            'username': 'Nama Pengguna',
        }