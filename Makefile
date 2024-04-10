create-venv:
	python3 -m venv .venv

.PHONY: activate-venv
activate-venv: .venv/bin/activate
	. .venv/bin/activate
install:
	pip3 install -r requirements.txt

test:
	pytest --cov

start:
	FLASK_ENV=development python3 manage.py run 

