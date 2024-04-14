create_venv:
	python3 -m venv .venv

.PHONY: activate-venv
activate_venv: .venv/bin/activate
	. .venv/bin/activate
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

a:
 	coverage run -m pytest > coverage_report.txt
 	coverage report -m | awk 'NR==1; NR>2{print $1,$2,$3,$4,$5}' >> coverage_report.txt
 	ls -l
 	cat coverage_report.txt