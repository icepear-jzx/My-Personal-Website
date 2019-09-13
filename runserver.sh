export FLASK_APP=flaskr
waitress-serve --port=80 --call 'flaskr:create_app' &
