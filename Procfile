release: python manage.py migrate
web: gunicorn Test_Django_setup.wsgi --log-file -

web: run-program waitress-serve --port=$PORT settings.wsgi:application
