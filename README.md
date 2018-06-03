Neptune
=======

About
-----
Neptune is a personal Django project, exploring the different tools that the framework has to offer.

Set-up
------
1. Install virtualenv with `pip install virtualenv`
1. Create a new environment from the given requirements file with `mkvirtualenv -r requirements.txt <env_name>`
1. Activate the environment with `workon env`

Run
---
1. In the `neptune_testing` directory run `python manage.py makemigrations`
1. Once the migrations are made, migrate with `python manage.py migrate`
2. The run the server with `python manage.py runserver`
