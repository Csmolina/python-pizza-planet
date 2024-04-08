create-venv:
	python3 -m venv venv

activate-venv:
	source venv/bin/activate
 
install:
	pip3 install -r requirements.txt

test:
	python3 manage.py test

start:
	FLASK_ENV=development
	python3 manage.py run 

