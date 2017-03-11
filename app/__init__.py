import os, binascii
from flask import Flask, session
from config import SQLALCHEMY_DATABASE_URI
from sqlalchemy import create_engine, MetaData

app = Flask(__name__)
app.config.from_object('config')

con = create_engine(SQLALCHEMY_DATABASE_URI)
m_data = MetaData(bind=con, reflect=True)

app.secret_key = binascii.hexlify(os.urandom(24))


# this code handles logging when running on heroku
if not app.debug and os.environ.get('HEROKU') is None:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/ontherise.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('microblog startup')

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('ontherise startup')

from app import views, models