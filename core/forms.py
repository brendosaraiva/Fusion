from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    assunto = forms.CharField(label="E-mail", max_length=100)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    # Recuperar informações dos campos do E-mail
    def send_email(self):
        nome = self.cleaned_data["nome"]
        email = self.cleaned_data["email"]
        assunto = self.cleaned_data["assunto"]
        mensagem = self.cleaned_data["mensagem"]

        conteudo = f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}"

        mail = EmailMessage(
            subject=assunto,
            body=conteudo,
            from_email="contato@fusion.com.br",  # Email que irá receber as mensagens
            to=["contato@fusion.com.br",],  # Caso tenha equipe de e-mail para dar suporte
            headers={"Reply-to": email}  # Responder o e-mail
        )

        mail.send()  # Envia o e-mail
