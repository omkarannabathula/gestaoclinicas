from django.db import models

class Clientes(models.Model):

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30, blank=True, null=True)
    sobrenome = models.CharField(max_length=30, blank=True, null=True)
    cnpj = models.CharField(max_length=11, blank=False, null=True)
    celular = models.CharField(max_length=9, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos', null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ["nome"]



# Create your models here.

class Gestor(models.Model):
    gestor_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    funcionario_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.nome


class Clinica(models.Model):
    clinica_id = models.AutoField(primary_key=True)
    nomefantasia = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=100)
    email = models.CharField(max_length=20, blank=True, null=True)
    contato = models.CharField(max_length=11, blank=True, null=True)
    especialidade = models.CharField(max_length=30, blank=True, null=True)



class Ativos(models.Model):
    id_ativo = models.SmallIntegerField(blank=True, null=True)
    nome = models.SmallIntegerField(blank=True, null=True)
    valor = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Contatos(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)
    sobrenome = models.CharField(max_length=50, blank=True, null=True)
    telefone = models.CharField(max_length=9, blank=True, null=True)
    celular = models.CharField(max_length=10, blank=True, null=True)
    id_cliente_empresas = models.ForeignKey('Empresas', models.DO_NOTHING, db_column='id_cliente', unique=False, blank=True, null=True)

  


class Empresas(models.Model):
    id_cliente = models.SmallIntegerField(primary_key=True)
    nome_fantasia = models.CharField(db_column='nome fantasia', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    nome_juridico = models.CharField(db_column='nome juridico', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    cnpj = models.CharField(max_length=11)



class Funcionarios(models.Model):
    id_func = models.SmallIntegerField(primary_key=True)
    nome = models.SmallIntegerField(blank=True, null=True)
    nr_func = models.SmallIntegerField(blank=True, null=True)





class IndicadoresNegativos(models.Model):
    id = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    questao = models.SmallIntegerField(blank=True, null=True)



class Lucratividade(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    lucro_liquido_anual = models.SmallIntegerField(blank=True, null=True)
    receita_total_anual = models.SmallIntegerField(blank=True, null=True)




class Passivos(models.Model):
    id_passivo = models.SmallIntegerField(primary_key=True)
    nome = models.SmallIntegerField(blank=True, null=True)

def __str__(self):
        return self.nome


class Roi(models.Model):
    id = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    receita = models.SmallIntegerField(blank=True, null=True)
    custo = models.SmallIntegerField(blank=True, null=True)
    item = models.SmallIntegerField(blank=True, null=True)





class TaxaConversao(models.Model):
    visitantes = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    id = models.SmallIntegerField(blank=True, null=True)
    conversoes = models.SmallIntegerField(blank=True, null=True)



class TicketMedioVendas(models.Model):
    id = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    total_receita = models.SmallIntegerField(blank=True, null=True)
    total_vendas = models.SmallIntegerField(blank=True, null=True)
    nr_compras = models.SmallIntegerField(blank=True, null=True)
    periodo = models.DateField(blank=True, null=True)




class Turnover(models.Model):
    id = models.SmallIntegerField(primary_key=True, blank=True, null=False)
    contratados = models.SmallIntegerField(blank=True, null=True)
    desligamentos = models.SmallIntegerField(blank=True, null=True)
    id_func_funcionarios = models.ForeignKey(Funcionarios, models.DO_NOTHING, db_column='id_func_funcionarios', unique=False, blank=True, null=True)

