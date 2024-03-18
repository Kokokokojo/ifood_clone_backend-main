from django.db import models as db

# Create your models here.

class Restaurant(db.Model):

    class States(db.TextChoices):
        ACRE = 'AC', 'Acre'
        ALAGOAS = 'AL', 'Alagoas'
        AMAPA = 'AP', 'Amapá'
        AMAZONAS = 'AM', 'Amazonas'
        BAHIA = 'BA', 'Bahia'
        CEARA = 'CE', 'Ceará'
        DISTRITO_FEDERAL = 'DF', 'Distrito Federal'
        ESPIRITO_SANTO = 'ES', 'Espírito Santo'
        GOIAS = 'GO', 'Goiás'
        MARANHAO = 'MA', 'Maranhão'
        MATO_GROSSO = 'MT', 'Mato Grosso'
        MATO_GROSSO_DO_SUL = 'MS', 'Mato Grosso do Sul'
        MINAS_GERAIS = 'MG', 'Minas Gerais'
        PARA = 'PA', 'Pará'
        PARAIBA = 'PB', 'Paraíba'
        PARANA = 'PR', 'Paraná'
        PERNAMBUCO = 'PE', 'Pernambuco'
        PIAUI = 'PI', 'Piauí'
        RIO_DE_JANEIRO = 'RJ', 'Rio de Janeiro'
        RIO_GRANDE_DO_NORTE = 'RN', 'Rio Grande do Norte'
        RIO_GRANDE_DO_SUL = 'RS', 'Rio Grande do Sul'
        RONDONIA = 'RO', 'Rondônia'
        RORAIMA = 'RR', 'Roraima'
        SANTA_CATARINA = 'SC', 'Santa Catarina'
        SAO_PAULO = 'SP', 'São Paulo'
        SERGIPE = 'SE', 'Sergipe'
        TOCANTINS = 'TO', 'Tocantins'


    name = db.CharField(max_length=75, blank=False, null=False)
    description = db.CharField(max_length=100, blank=False, null=False)
    logo = db.ImageField(upload_to="restaurants/logos/%Y/%m/%d", blank=False, null=False)
    street = db.CharField(max_length=75, blank=False, null=False)
    neighborhood = db.CharField(max_length=75, blank=False, null=False)
    number = db.CharField(max_length=100, blank=False, null=False)
    city = db.CharField(max_length=75, blank=False, null=False)
    state = db.CharField(max_length=3, choices=States.choices, blank=False, null=False)
    zip_code = db.CharField(max_length=8, blank=False, null=False)
    
    manager = db.ForeignKey('users.customuser', on_delete= db.SET_NULL, null=True, blank=True)

    is_active = db.BooleanField(default=True)

    def __str__(self):
        return self.name
