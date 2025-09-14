import uuid  # Gera valores hexadecimais aleatórios... Excelente para renomear arquivos conflitantes com hexadecimal.
from django.db import models
from stdimage import StdImageField


def get_file_path(_instance_, filename):  # _instance_ > é a instância do modelo que está chamando upload_to.
    ext = filename.split(".")[-1]  # recebe um arquivo e quebra o texto pegando a última parte dele.
    filename = f'{uuid.uuid4()}.{ext}'  # gera um hexadecimal e conecta com a parte tirada.
    return filename


class Base(models.Model):
    criados = models.DateField("Criação", auto_now_add=True)  # auto_now_add=True: Define a data no momento de criação
    modificado = models.DateField("Atualização", auto_now=True)  # auto_now=True: Altera somente as datas de modificação
    ativo = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ("lni-cog", "Engrenagem"),
        ("lni-stats-up", "Gráfico"),
        ("lni-users", "Usuários"),
        ("lni-layers", "Design"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Foguete")
    )

    servico = models.CharField("Serviço", max_length=100)
    descricao = models.TextField("Descrição", max_length=200)
    icone = models.CharField("Icone", max_length=12, choices=ICONE_CHOICES)

    class Meta:
        # Alteram o nome da classe (Servico) na apresentação do painel administrativo.
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField("Cargo", max_length=100)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField("Nome", max_length=100)
    # ForeignKey(app.chave_estrangeira, verbose_name="Nome_de_definição", on_delete=models.CASCADE)
    # o **on_delete=models.CASCADE age apenas quando apaga um registro específico da tabela relacionada. Exemplo:
    # "Desenvolvedor Back-end.", todos os registros relacionados a ele serão apagados com ele.
    cargo = models.ForeignKey("core.Cargo", verbose_name="Cargo", on_delete=models.CASCADE)
    bio = models.TextField("Biografia", max_length=300)
    # StdImageField > Irá criar um diretório chamado media e um subdiretório com nome "equipe" definido em upload_to,
    # de onde pegará as fotos.
    imagem = StdImageField("Imagem", upload_to=get_file_path, variations={
        "thumb": {
            "width": 480,
            "height": 480,
            "crop": True
        }
    })
    facebook = models.CharField("Facebook", max_length=100, default="#")
    twitter = models.CharField("Twitter", max_length=100, default="#")
    instagram = models.CharField("Instagram", max_length=100, default="#")

    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return self.nome


class Feature(Base):
    ICONE_CHOICES = (
        ("lni-rocket", "Foguete"),
        ("lni-laptop-phone", "Usuários"),
        ("lni-cog", "Engrenagem"),
        ("lni-layers", "Design"),
        ("lni-stats-up", "Template"),
        ("lni-mobile", "Formulário"),
    )

    icone = models.CharField("Icone", max_length=20, choices=ICONE_CHOICES)
    feature = models.CharField("Feature", max_length=100)
    descricao = models.TextField("Descricao", max_length=300)

    class Meta:
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"

    def __str__(self):
        return self.feature


class Cliente(Base):
    nome = models.CharField("Nome", max_length=30)
    titulo = models.CharField("Título", max_length=100)
    mensagem = models.CharField("Mensagem", max_length=300)
    nota = models.IntegerField("Nota")
    imagem = StdImageField("Imagem", upload_to=get_file_path, variations={
        "thumb": {
            "width": 72,
            "height": 72,
            "crop": True
        }
    })

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

