release: python manage.py migrate && python manage.py compilescss --use-processor-root && python manage.py collectstatic --noinput && python manage.py compilemessages

web: uwsgi --master --enable-threads --http-socket :$PORT --static-map /static=/vol/static --static-map /media=/vol/media --module kausal_web.wsgi
