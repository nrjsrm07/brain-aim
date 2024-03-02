python -m venv env
env/scripts/activate
pip install -r requirements.txt

If we install any new package than we have to run this command to add that package in requirements.txt-
pip freeze > requirements.txt 

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver