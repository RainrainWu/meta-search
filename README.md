# meta-search

A meta-searching engine combine the searching result from google, yahoo, and baidu.

# Prerequisites
- Python 3.8

# Getting Started
- Run the server
```
$ cd metasearch
$ poetry run python manage.py runserver
```
The server should be run within a virtual environment created by **poetry**.

- Search keyword
```
$ http --json POST http://127.0.0.1:8000/v1/histories keyword=mur
```
The meta-searching engine was implemented via **Selenium** to attempt human-behavior-like simulation and asynchronous requests, this may take you 30 to 60 seconds to download the appropriate webdriver for the first time.

- Check searching histories
```
$ http GET 127.0.0.1:8000/v1/histories
```
The meta-searching engine will automatically store all searching histories into the local `db.sqlite3` file, and fetch the result if the currently searched keyword was found instead of using webdriver.