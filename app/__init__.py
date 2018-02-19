from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'givemeaccess'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = 'ee4afaefc31ed1'
app.config['MAIL_PASSWORD'] = 'b1d908539fa0de'
mail = Mail(app)

from app import views