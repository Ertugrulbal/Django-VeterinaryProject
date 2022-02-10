cd # Veterinary Application using Django

## Dependencies used in the project

- Python 3.9.5
- PostgreSQL 14.1

## Project Setup

- Clone the project with `git clone https://github.com/Ertugrulbal/Django-VeterinaryProject.git && cd Django-VeterinaryProject`
- Create virtual environment with `virtualenv --python=3.9 .venv` and activate it with `source .venv/bin/activate`
- Enter the ecommerce folder with `cd vetproject`
- Install dependencies with `pip install -r requirements.txt`
- Create server, database and superuser with the Postgresql. (If you want to do database operations with a gui, you can additionally use pgAdmin.)
- Execute the migrate process with `python manage.py migrate`
- Fill in the contents of the [`.env.dist`](ecommerce/.env.dist) file and copy it as `.env`

### Inside of the ".env" File

- SECRET_KEY in the .env file can be generated with the following command. <br> `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- DEBUG variable should be True only during project development. 
- The parameters in the DATABASE_URL variable in the .env file are the superuser username and password, the IP and port specified for the server, and the database name, respectively.

### Migrations for SQL

In order for the changes to be created in the form of SQL Tables, the migrate operation must be performed. The migration process consists of the following two steps. 

- Creating migration files: `python manage.py makemigrations`
- The resulting files create the necessary tables in SQL database: `python manage.py migrate`
### Django Admin Panel

In order to enter the admin panel, it is necessary to create a super user. It can be done with the following command: `python manage.py createsuperuser`. Then type email and password.
### Django Rest Framework API Management
In order to enter a API page, you must be a logged in.
- We have two api; pet and petOwner.
- If you logged in, you can do CRUD Operations.
> We also made a filter operations. If you want to filtration on;
- Pet API, you can fill a filter fields which are Name, Type and Variety 
- PetOwner API, you can fill a filter field which is PetOwner Name
## Run 

Run `python manage.py runserver ip_you_want:port_you_want` and go to [`http://ip_you_want:port_you_want`](ip_you_want:port_you_want) from the browser.

Ex.: Run `python manage.py runserver 0.0.0.0:5252` and go to [`http://0.0.0.0:5252`](http://0.0.0.0:5252) from the browser.

> Note: If ip and port are not specified, it will work on the default ip(127.0.0.1) and port(8000). Make sure that the ip address entered in "ip_you_want" is in ALLOWED_HOSTS variable in the [`.env`](ecommerce/.env) file.
### Apps
## Core

It contains functions, classes and constants to be used as a basis in the core.

##Pet
It contains pet model and petOwner model for pets.
