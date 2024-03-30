from django.db import models as db

# Create your models here.


class Address(db.Model):

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


    class Type(db.TextChoices):
        HOUSE = 'H', 'House'
        WORK = 'W', 'Work'
        ANOTHER = 'AN', 'Another'




    name = db.CharField(max_length=75, blank=False, null=False)
    street = db.CharField(max_length=75, blank=False, null=False)
    neighborhood = db.CharField(max_length=75, blank=False, null=False)
    number = db.CharField(max_length=75, blank=False, null=False)
    complement = db.CharField(max_length=75, blank=True, null=True)
    city = db.CharField(max_length=75, blank=False, null=False)
    zip_code = db.CharField(max_length=8, blank=False, null=False)

    user = db.ForeignKey('users.CustomUser', related_name='addresses', on_delete=db.CASCADE, null=True, blank=False)
    state = db.CharField(max_length=3, choices=States.choices, blank=False, null=False)
    type_of = db.CharField(max_length=3, choices=Type.choices, blank=True, null=True)

    is_selected = db.BooleanField(default=False)

    is_active = db.BooleanField(default=True)


    def __str__(self):
        return self.name