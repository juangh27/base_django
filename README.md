# base_django
Django local install

python3 -m venv .venv

. .venv/bin/activate

python manage.py migrate

python manage.py createsuperuser

104.236.208.3

sudo ufw allow 8000

python manage.py runserver your_server_ip:8000