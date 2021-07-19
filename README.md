### task_endpoint

The following are the steps to be taking to test this endpoint:
clone the repository from github using:
- [x] ```git clone https://github.com/Favourkass/Dro_health_task_endpoint.git```

next run the following:

- [x] ``` pip install -r requirements.txt ```

then makemigrations

- [x] ``` python manage.py makemigrations```
- [x] ``` python manage.py migrate```
- [x] ``` python manage.py makemigrations test_api```
- [x] ``` python manage.py migrate test_api```

next:

- [x] ```python manage.py runserver 8080```

then register a user with the following url:

- [x] ```http://localhost:8080/women-health/api/rest-auth/registration/```

and login with:

- [x] ```http://localhost:8080/women-health/api/rest-auth/login/```

then proceed to the create cycle endpoint:

- [x] ```http://localhost:8080/women-health/api/create-cycles/```

and fill in your data

finally proceed to the cycle-event endpoint:

- [x] ```http://localhost:8080/women-health/api/cycle-event?date=2021-20-19```

you can change the details after date as you see fit


to run unittest:
- [x] ```python manage.py test test_api```


