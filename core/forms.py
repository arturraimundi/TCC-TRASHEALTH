from django import forms
from .models import PontodeColeta

class PontodeColetaForm(forms.ModelForm):
    class Meta:
        model = PontodeColeta
        fields = ['titulo', 'local', 'descricao', 'imagem', 'coordenadaX', 'coordenadaY']



class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite seu e-mail aqui',
            'id': 'email',
        }),
        label="E-mail"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite sua senha aqui',
            'id': 'senha',
        }),
        label="Senha"
    )
