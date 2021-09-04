import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "mysecret"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATION = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get(
        'MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['microblogger.flask@gmail.com']
    POSTS_PER_PAGE = 5
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get(
        'ELASTICSEARCH_URL') or 'http://localhost:9200'
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')


'''
export FLASK_DEBUG=1

export MAIL_SERVER=smtp.googlemail.com
export MAIL_PORT=587
export MAIL_USE_TLS=1
export MAIL_USERNAME='microblogger.flask@gmail.com'
export MAIL_PASSWORD='Sidmicroblogger@123'
'''
