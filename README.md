# event-server

Backend that provides a thirdparty to report events.

Currently an event is defined as:
Event
  - title
  - description
  - created (date of creation)
  - updated (date of last update)
  - Category
    - title
    - description
    - created (date of creation)
    - updated (date of last update)
    
The REST api is exposed through:

remotely: https://events-rep.herokuapp.com/v1/

locally: http://localhost:8000/v1/

### How to deploy project in Heroku

- Create a new project
- Either use the heroku CLI or web interface to push this repository to heroku
- Add the required buildpacks on heroku web interface.

```python
heroku/python
https://github.com/cyberdelia/heroku-geo-buildpack.git
https://github.com/heroku/heroku-buildpack-apt
```

The default path to the postgres database is being used so no further configuration is needed.

### How to run locally

To run the project locally a few dependencies are required:
```python
pipenv
postgres
libgeos
libgdal
libproj
```

Running the following command should take care of the installation of all external dependencies.
```python
pipenv install
```

The full path to the postgres database is the following:
```python
local_database_path = "postgres://{}:{}@localhost:5432/event_reporting_db".format(os.environ["DJANGO_EVENT_USER"], os.environ["DJANGO_EVENT_PW"])
```
A database called "event_reporting_db" must be created (CREATE DATABASE event_reporting_db)
The user and password of the database are exposed to the application through environment variables:

```python
export DJANGO_EVENT_USER='postgres'   
export DJANGO_EVENT_PW='password'
```

Postgis (https://postgis.net/) then can be installed through pgc
```python
  #/Users/user/PostgreSQL/pgc install postgis
```
Enable the extension by connecting to the postgres command line interface and enable the extension:

```python
create extension postgis;
```

Finally start the server

```python
python manage.py runserver
```







