# base_django
Django local install

python3 -m venv .venv

. .venv/bin/activate

python manage.py migrate

python manage.py createsuperuser

104.236.208.3

sudo ufw allow 8000

python manage.py runserver your_server_ip:8000
python manage.py runserver 104.236.208.3:8000



------------------------------------------

sudo ln -s /etc/nginx/sites-available/juangh.ing /etc/nginx/sites-enabled/

mkdir -p /var/www/juangh.ing/html

certbot --nginx -d juangh.ing -d juangh.ing

ln -s /etc/nginx/sites-available/<your-config-file> /etc/nginx/sites-enabled/



----------------api------------

GET /books/: Lists all books.
POST /books/: Creates a new book.
GET /books/1/: Retrieves the book with pk=1.
PUT /books/1/ or PATCH /books/1/: Updates the book with pk=1.
DELETE /books/1/: Deletes the book with pk=1.