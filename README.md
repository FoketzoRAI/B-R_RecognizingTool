# Deploy instructions

1. Install [PostgreSQL](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads "PostgreSQL Database Download")
    1. Open pgAdmin4
    2. Create database for your project.
2. Create *virtual environment* **(venv)**:
    1. For Windows: `py -m venv venv`
    2. For Linux: `python3 -m venv venv`
3. Activate venv:
    1. For Windows: `venv\Scripts\activate`
    2. For Linux: `source venv/bin/activate`
4. Install package dependencies:<br>
   `pip install psycopg2 django`
5. Change your settings according to your PostgreSQL:
    1. Open *settings.py*
    2. Find ***DATABASE*** variable
    3. Change it:
~~~python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'name_of_database_in_PSQL',
        'USER' : 'user_in_PSQL',
        'PASSWORD' : 'user_password_in_PSQL',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}       
~~~
6. Set up your DB to PSQL by these commands:
    1. `py manage.py makemigrations` - saving initial migrations
    2. `py manage.py migrate` - sending migrations to DB
    3. `py manage.py createsuperuser` - create Administrator.
       1.   Enter your desired username and press enter.
`Username: admin`
        2. You will then be prompted for your desired email address: `Email address: admin@example.com`
        3. The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
7. Now, you can start the server!
`python manage.py runserver`