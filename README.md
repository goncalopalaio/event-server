# event-server

Backend that provides a thirdparty to report events.
    
The REST api is exposed through:

https://events-rep.herokuapp.com/v1/

The admin interface can be reached at:

https://events-rep.herokuapp.com/admin/
user:admin password: password1234

A postman collection with a few filtering queries is shared here:

https://documenter.getpostman.com/view/4266504/RW1dExc8

Supported:
- Filter by category
- Filter by author
- Filter by position and distance


Mobile client at: https://github.com/goncalopalaio/event-mobile

## A few notes

### Current state of development

Developing into master branch directly since I'm the only developer at the time. Pull requests should be used going forward.

This project uses the Django REST framework and at this time, the web browsable API feature is enabled and exposed without any kind of authentication. This is a feature that should be disabled later, but makes it easy to explore the API using a web browser by opening 
https://events-rep.herokuapp.com/v1/ 

DEBUG mode should be disabled.

Currently there's a few pydoc strings but nothing too relevant.

Haven't created any tests at the time for the REST api but this is a point to keep in mind going forward.

### Missing functionality

An access key or auth2 should be implemented.  There's no user authentication implemented at this time. The events can be changed by anyone.

### About the mobile client

Available at https://github.com/goncalopalaio/event-mobile

### How to deploy project in Heroku

- Create a new project
- Either use the heroku CLI or web interface to push this repository to heroku
- Add the required buildpacks on heroku web interface.

```python
heroku/python
https://github.com/cyberdelia/heroku-geo-buildpack.git
https://github.com/heroku/heroku-buildpack-apt
```

Load default data, such as categories and event states:

```python
heroku run python  manage.py loaddata defaults.json
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
(using a migration operation would be a better option)

Load default data:

```python
python manage.py loaddata defaults.json
```

Finally start the server

```python
python manage.py runserver
```







