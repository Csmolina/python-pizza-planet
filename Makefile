create_venv:
	python3 -m venv .venv

install:
	pip3 install -r requirements.txt

test:
	pytest --cov

start:
	FLASK_ENV=development python3 manage.py run 

init_db:
	python3 manage.py db init
	python3 manage.py db migrate
	python3 manage.py db upgrade

populate:
	python3 manage.py populate
