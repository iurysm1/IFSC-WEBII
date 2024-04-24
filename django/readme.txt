Para rodar a aplicação:

1-Descompacte o arquivo na sua pasta de trabalho;
2-Crie o ambiente virtual: python -m venv django-env
3-Instale as bibliotecas: pip install -r requirements.txt
4-Ingresse na pasta do projeto e execute as migrações:
	python manage.py makemigrations
	python manage.py migrate
5-Para subir a aplicação:
	python manage.py runserver