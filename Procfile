web: gunicorn emas_v2 emas_v2.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate