# PHEV Electric Vehicle Scraping Backend Application
[![Build Status](https://travis-ci.com/eneakllomollari/pscraper-db.svg?token=dyCCbKsyaqSXpEtQ3kCk&branch=master)](https://travis-ci.com/eneakllomollari/pscraper-db)
## Design

Pscraper backend is designed using:

* Django
* Django REST framework
* MySQL

## API

This application is deployed on [Heroku](http://pscraper.herokuapp.com) and [App Engine](http://phev-scraping.appspot.com/)

The API endpoints can be found [here](https://pscraper.herokuapp.com/api/v1/) or [here](https://phev-scraping.appspot.com/api/v1/). <br>
For the full API documentation go to the Pscraper API site [here](http://pscraper.herokuapp.com/api/v1/docs) or [here](https://phev-scraping.appspot.com/api/v1/docs). 

## Table Schema

The MySQL instance is hosted in GCP's Cloud SQL
There are 3 main MySQL tables containing the data:

### pscraper_vehicle

| Column     | Type         | Attributes | Null | Default | Extra | Links to                                                          |
|------------|--------------|------------|------|---------|-------|-------------------------------------------------------------------|
| id         | int(11)      |            | No   |         |       | auto_increment                                                    |
| vin        | varchar(17)  |            | No   |         |       |                                                                   |
| listing_id | varchar(255) |            | No   |         |       |                                                                   |
| make       | varchar(255) |            | No   |         |       |                                                                   |
| model      | varchar(255) |            | Yes  | NULL    |       |                                                                   |
| trim       | varchar(255) |            | Yes  | NULL    |       |                                                                   |
| body_style | varchar(255) |            | Yes  | NULL    |       |                                                                   |
| mileage    | int(11)      |            | Yes  | NULL    |       |                                                                   |
| year       | int(11)      |            | Yes  | NULL    |       |                                                                   |
| price      | double       |            | Yes  | NULL    |       |                                                                   |
| first_date | date         |            | No   |         |       |                                                                   |
| last_date  | date         |            | No   |         |       |                                                                   |
| duration   | int(11)      |            | No   |         |       |                                                                   |
| seller_id  | int(11)      |            | No   |         |       | -> pscraper_seller. id<br>ON UPDATE RESTRICT<br>ON DELETE RESTRICT |

### pscraper_seller

| Column       | Type         | Attributes | Null | Default | Extra          | Links to |
|--------------|--------------|------------|------|---------|----------------|----------|
| id           | int(11)      |            | No   |         | auto_increment |          |
| phone_number | varchar(31)  |            | No   |         |                |          |
| address      | varchar(255) |            | No   |         |                |          |
| name         | varchar(255) |            | No   |         |                |          |
| latitude     | double       |            | Yes  | NULL    |                |          |
| longitude    | double       |            | Yes  | NULL    |                |          |

### pscraper_history

| Column    | Type        | Attributes | Null | Default | Extra          | Links to                                                          |
|-----------|-------------|------------|------|---------|----------------|-------------------------------------------------------------------|
| id        | int(11)     |            | No   |         | auto_increment |                                                                   |
| vin       | varchar(17) |            | No   |         |                |                                                                   |
| price     | double      |            | Yes  | NULL    |                |                                                                   |
| date      | date        |            | No   |         |                |                                                                   |
| seller_id | int(11)     |            | No   |         |                | -> pscraper_seller. id<br>ON UPDATE RESTRICT<br>ON DELETE RESTRICT |

## Environment set up

1. Ensure you have `python3.7` installed

```shell script
$ python3.7 --version
Python 3.7.7
``` 

2. Export the necessary environment variables `DJANGO_SECRET_KEY` and `DEFAULT_DATABASE_PASSWORD` 

```shell script
export DJANGO_SECRET_KEY={{ DJANGO_SECRET_KEY_HERE }}
export PSCRAPER_PASSWORD={{ PSCRAPER_PASSWORD_HERE }}
```

3. Set up the virtual environment

```shell script
$ python3.7 -m venv venv3
$ source venv3/bin/activate
(venv3) $ pip install -r requirements. txt -U
(venv3) $ cd pscraperdb
``` 

## Run Development Server locally

```shell script
(venv3) $ ./manage.py runserver
```

## Connect to the MySQL database shell

**This is a direct connection to the MySQL database**
```mysql
(venv3) $ . /manage. py dbshell
... 
Type 'help; ' or '\h' for help. Type '\c' to clear the current input statement. 

mysql> SELECT make, model, price, first_date, duration FROM pscraper_vehicle WHERE price>220000; 
+---------+--------+--------+------------+----------+
| make    | model  | price  | first_date | duration |
+---------+--------+--------+------------+----------+
| Porsche | Taycan | 231950 | 2020-03-12 |       40 |
| Porsche | Taycan | 245500 | 2020-03-30 |       22 |
| Porsche | Taycan | 245500 | 2020-03-30 |       22 |
| Porsche | Taycan | 223270 | 2020-04-03 |       18 |
+---------+--------+--------+------------+----------+
4 rows in set (0. 23 sec)

mysql> SELECT phone_number, address, name FROM pscraper_seller WHERE address LIKE '%Davis%'; 
+--------------+------------------------------+--------------------------------------------+
| phone_number | address                      | name                                       |
+--------------+------------------------------+--------------------------------------------+
| 8312693039   | 1980 N Davis Rd, Salinas, CA | Gold Star Motors                           |
| 5305542723   | 5009 Chiles Rd, Davis, CA    | Hanlees Nissan                             |
| 5305544306   | 4989 Chiles Rd, Davis, CA    | Hanlees Davis Chevrolet Nissan             |
| 5305549791   | 4318 Chiles Rd, Davis, CA    | Hanlees Davis Chryler Dodge Jeep RAM & Kia |
| 5302045536   | 4343 Chiles Rd, Davis, CA    | Shottenkirk Honda of Davis                 |
+--------------+------------------------------+--------------------------------------------+
5 rows in set (0. 16 sec)

mysql> SELECT price, date, seller_id FROM pscraper_history WHERE price>245000 AND date='2020-04-16'; 
+--------+------------+-----------+
| price  | date       | seller_id |
+--------+------------+-----------+
| 245500 | 2020-04-16 |      1431 |
| 245500 | 2020-04-16 |      1431 |
| 245500 | 2020-04-16 |      1431 |
+--------+------------+-----------+
3 rows in set (0. 17 sec)
``` 

### List all available management commands

```shell script
(venv3) $ ./manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[rest_framework]
    generateschema

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver
```
