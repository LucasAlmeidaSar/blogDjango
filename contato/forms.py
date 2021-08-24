import requests
from django.forms import ModelForm, Textarea, TextInput, EmailInput
from contato.models import Contato


class FormContato(ModelForm):
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
                'conteudo_contato',
                'Marque o recaptcha.'
            )

        data = self.cleaned_data
        nome = data.get('nome_contato')

        if len(nome) < 5:
            self.add_error(
                'nome_contato',
                'O nome precisa ter mais de 5 caracteres'
            )

    class Meta:
        model = Contato
        fields = ('nome_contato', 'email_contato', 'assunto_contato', 'conteudo_contato',)
        labels = {
            'nome_contato': '',
            'email_contato': '',
            'assunto_contato': '',
            'conteudo_contato': '',
        }
        widgets = {
            'nome_contato': TextInput(attrs={'placeholder': 'Nome completo'}),
            'email_contato': EmailInput(attrs={'placeholder': 'E-mail'}),
            'assunto_contato': TextInput(attrs={'placeholder': 'Assunto da mensagem'}),
            'conteudo_contato': Textarea(attrs={'placeholder':'Digite sua mensagem', 'style':'resize:none;'}),
        }



