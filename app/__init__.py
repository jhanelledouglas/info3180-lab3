from flask import Flask
from flask_mail import Mail
from .config import Config

app = Flask(__name__)

app.config.from_object(Config)

# app.config['SECRET_KEY']='Som3$ec5etK*y'
# app.config['MAIL_SERVER']='smtp.mailtrap.io'
# app.config['MAIL_PORT'] = 2525
# app.config['MAIL_USERNAME'] = '3bf118dcb01107'
# app.config['MAIL_PASSWORD'] = 'e3d01da6b3ba80'


mail = Mail(app)


mail = Mail(app)
from app import views


