# House-Boat
House Boat booking website


# How to run
- Firstly install python, pip and clone the folder locally and open it in terminal.
- Next run,
```
pip install -r requirements.txt
```
- setup database
> we are sqlite3 for now
```
python manage.py migrate
```
- next collect all static to static files directory
```
python manage.py collectstatic --clear
```
- finally runserver
```
python manage.py runserver
```