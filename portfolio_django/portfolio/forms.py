from django import forms
from .models import Message


class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={
                'placeholder': 'Votre nom',
                'class': 'form-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'votre@email.com',
                'class': 'form-input'
            }),
            'sujet': forms.TextInput(attrs={
                'placeholder': 'Sujet du message',
                'class': 'form-input'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Votre message...',
                'rows': 5,
                'class': 'form-input'
            }),
        }
        labels = {
            'nom': 'Nom',
            'email': 'Email',
            'sujet': 'Sujet',
            'message': 'Message',
        }
