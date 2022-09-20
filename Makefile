install:
	pip3 install -r requirements.txt

migrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

superuser:
	python3 manage.py createsuperuser

shell:
	python3 manage.py shell

serve:
	python3 manage.py runserver

test:
	pytest --cov-report term-missing --cov=src/api/V1 -p no:warnings