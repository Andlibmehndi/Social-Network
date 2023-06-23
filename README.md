# Django RESTful API 

Project is using 3rd party package api call. Create account on (https://www.abstractapi.com/) and replace your api keys in  env file 

### **Steps To run run project** 
Env template present in repo just rename to env
```
.env.template >> .env
```
Install the dependencies and verify django.
```sh
pip install -r .\requirements.txt
django-admin
```

Create database & it's schema using migration
```sh
python ./manage.py makemigrations
python ./manage.py migrate
```

Run the project
```sh
python .\manage.py runserver
```

Test case
```sh
coverage run .\manage.py test || python .\manage.py test
coverage report
coverage html
```

### Api endpoints
| Method | Endpoint |
| ------ | ------ |
| POST | /user/signup |
| GET | /user/ping |
| GET | /user/details |
| POST | /user/login |
| POST | /user/login-refresh |
| POST | /post/create |
| GET | /post/ |
| PUT | /post/{id}/ |
| DEL | /post/{id}/ |
| PUT/POST | /post/{id}/toggle/ |