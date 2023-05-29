# Nicasource api

## How to run??
 - Make sure you have installed `docker` and `docker-compose`
 - Run 1 `docker-compose build`
 - Run 2 `docker-compose up -d`
 - Run 3 `docker-compose exec web python manage.py makemigrations` 
 - Run 3 `docker-compose exec web python manage.py migrate` 
 - Head over to http://0.0.0.0:8000