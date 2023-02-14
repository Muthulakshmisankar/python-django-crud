

open terminal, execute the following command to create python project and create app
1.workon djangoenv(i.e.,venvtest)
2.django-admin startproject restfulapicrud
3.python manage.py startapp empApi

create virtual environment:

>pip install virtualenv
>virtualenv venvtest
>cd  venvtest/Scripts
>activate
> cd..
>cd..
pip install django
django-admin --version

>cd venvtest/Scripts
>activate
>cd../../
>python manage.py runserver


(venvtest) C:\django rest api\restfulapicrud>python manage.py startapp empApi

pip install djangorestframework
setup pgadmin, postgresql --> pip install psycopg2 
Add connection in settings.py, then execute the following command it will start the development server at http://127.0.0.1:8000/

>python manage.py migrate

After model creation:

python manage.py makemigrations empApi
python manage.py migrate

