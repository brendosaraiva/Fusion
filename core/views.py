from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = "index.html"
    form_class = ContatoForm  # Recebe o tipo de classe de formulário que está sendo utilizado.
    success_url = reverse_lazy("index")  # Onde a mensagem de sucesso será apresentado.

    # sobreescreve o método de TemplateView (Overrides)
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)  # Recupera o contexto.
        # Extraí os dados dos modelos de Servico e Funcionario e os adicionam ao contexto.
        context["servicos"] = Servico.objects.order_by("?").all()  # order_by("?") -> "?" ordena aleatoriamente, seja:
        # id, ordem alfabética... Aleatoriamente troca a ordem dos dados.
        context["funcionarios"] = Funcionario.objects.order_by("?").all()

        # dividir features em duas
        features = Feature.objects.order_by("?").all()
        total = len(features)

        # Como "futuramente" o sistema possa ter mais features
        context["features_left"] = features[:int(total/2)]  # a primeira seção recebe a metade dos itens
        context["features_right"] = features[int(total/2):int(total)]  # a segunda recebe os últimos itens

        # Está pronto para iterar os objetos no index
        return context

    # Se o formulário for válido
    def form_valid(self, form, *args, **kwargs):
        form.send_email()  # Vai enviar o E-mail
        messages.success(self.request, "E-mail enviado com sucesso")  # Exibirá uma mensagem dizendo que funcionou
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # Uma vez validado, retornará o formulário com
        # as informações para serem apresentadas no template "index".

    # Se o formulário for inválido
    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail")  # Exibirá uma mensagem dizendo que falhou
        return super(IndexView, self).form_valid(form, *args, **kwargs)  # Uma vez validado, retornará o formulário com
        # as informações de erro para serem apresentadas no template "index".
