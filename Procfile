release: python manage.py migrate && python manage.py compilemessages

web: gunicorn kausal_web.wsgi --log-file -
