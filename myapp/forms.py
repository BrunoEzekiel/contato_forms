from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nome', 'email', 'mensagem']
        labels = {
            'nome': 'Nome',
            'email': 'E-mail',
            'mensagem': 'Mensagem'
        }