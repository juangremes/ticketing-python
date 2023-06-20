# TODO: add auth Flask app code, see if we need CORS
#  add wsgi.py or gunicorn_conf.py with config
#  add entrypoint.sh calling gunicorn (Dockerfile entrypoint)
from flask import Flask


app = Flask(__name__)


@app.get('/')
def comments_get():
    return "Hello from auth!\n", 200
