from platform import system
from subprocess import call

match system():

    case 'Windows':
        call('cls', shell=True)
        call(f'python manage.py makemigrations', shell=True)
        call(f'python manage.py migrate', shell=True)
    case _:
        call('clear', shell=True)
        call(f'python3 manage.py makemigrations', shell=True)
        call(f'python3 manage.py migrate', shell=True)