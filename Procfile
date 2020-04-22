release: python manage.py migrate && python manage.py compilescss --use-processor-root && python manage.py compilemessages

web: uwsgi --master --enable-threads --http-socket :8000 --static-map /static=/vol/static --static-map /media=/vol/media --module kausal_web.wsgi
