import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    MAIL_SERVER="sandbox.smtp.mailtrap.io"
    MAIL_PORT=2525
    MAIL_USERNAME="2b4a55b5d491e8"
    MAIL_PASSWORD="503f2262c33deb"
    SECRET_KEY="Random#765"
