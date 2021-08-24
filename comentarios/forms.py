import requests
from django.forms import ModelForm, TextInput, EmailInput, Textarea
from comentarios.models import Comentario

class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LdWwh0cAAAAADcs0V7L9cSNFFggIfW3wdyXFgDu',
                'response': recaptcha_response
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(
                'conteudo_comentario',
                'Marque o recaptcha.'
            )

        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('conteudo_comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'O nome precisa ter mais de 5 caracteres'
            )

    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'conteudo_comentario')
        labels = {
            'nome_comentario': '',
            'email_comentario': '',
            'conteudo_comentario': '',
        }
        widgets = {
            'nome_comentario': TextInput(attrs={'placeholder': 'Nome completo'}),
            'email_comentario': EmailInput(attrs={'placeholder': 'E-mail'}),
            'conteudo_comentario': Textarea(attrs={'placeholder': 'Digite sua mensagem', 'style': 'resize:none;'}),
        }