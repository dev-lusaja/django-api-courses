IMAGE = devlusaja-django-api-courses:latest
CONTAINER = django_container

.PHONY: run

build:
	@docker build -t ${IMAGE} .

up:
	@docker run --rm --name ${CONTAINER} -p 8000:8000 -v ${PWD}/api:/code ${IMAGE}

migrate:
	@docker run --rm -v ${PWD}/api:/code ${IMAGE} python3 manage.py migrate

migrations:
	@docker run --rm -ti -v ${PWD}/api:/code ${IMAGE} python3 manage.py makemigrations courses

super-user:
	@docker run --rm -ti -v ${PWD}/api:/code ${IMAGE} python3 manage.py createsuperuser

create-project:
	docker run --rm -it -v ${PWD}/api:/code ${IMAGE} django-admin startproject project .

create-courses:
	docker run --rm -it -v ${PWD}/api:/code ${IMAGE} django-admin startapp courses

data:
	docker run --rm -it -v ${PWD}/api:/code ${IMAGE} python3 manage.py loaddata data.json
