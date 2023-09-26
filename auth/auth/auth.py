# TODO: add auth Flask app code, see if we need CORS
#  add wsgi.py or gunicorn_conf.py with config
#  add entrypoint.sh calling gunicorn (Dockerfile entrypoint)
#  OR add all that config inside the entrypoint.sh directly: gunicorn app:app -w 2 --threads 2 -b 0.0.0.0:8000
from . import create_app


app = create_app()
if __name__ == "__main__":
    app.run(host='0.0.0.0')

