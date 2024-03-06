from collections import defaultdict
from django.forms import ValidationError
from users.models import CustomUser, Address
from django.db.models import Q


class CustomUserValidator:
    def __init__(self, data, errors=None, ErrorClass=None):
        self.errors = defaultdict(list) if errors is None else errors
        self.ErrorClass = ValidationError if ErrorClass is None else ErrorClass
        self.data = data
        self.clean()


    def clean(self, *args, **kwargs):
        
        self.check_edit_personal_info()


        if self.errors:
            raise self.ErrorClass(self.errors)
    

    def check_edit_personal_info(self):

        first_name = self.data.get('first_name', '')
        # last_name = self.data.get('last_name', '')
        # cpf = self.data.get('cpf', '')

        if first_name == "":
            self.errors['first_name_blank'].append('Primeiro nome não pode ser vazio')

        # if cpf == "":
        #     self.errors['cpf_blank'].append('CPF não pode ser vazio')