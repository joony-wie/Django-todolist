Django Todolist
============================
윈터코딩 개발 과제 웹 - TODO list 만들기(Django)

Installation
============

1. Clone ``Django-todolist``

    ``$ git clone https://github.com/encia200/Django-todolist.git``
    
    ``$ cd Django-todolist``

2. Create Virtual enviroment
    
    if you don't have ``python3-venv`` 

    ``$ sudo apt-get install python3-venv``
    ``$ python3 -m venv todolistvenv``
    
3. Activate you virtual enviroment
   
    ``$ source todolistvenv/bin/activate``

4. Install ``requirements.txt``

    Before installing Django, you should make sure you have the latest version of ``pip``
    
    ``$ python3 -m pip install --upgrade pip``
    
    and then,
    
    ``$ pip install -r requirements.txt``
    
5. Apply your migration

    ``$ python manage.py migrate``

5. Run server

    ``$ python manage.py runserver``
