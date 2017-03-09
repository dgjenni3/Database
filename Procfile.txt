web: gunicorn app:app
init: python db_create.py
destroy: python db_destroy.py