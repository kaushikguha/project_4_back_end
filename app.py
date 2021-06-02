
from flask import Flask, jsonify

from resources.pmt import pmt

from resources.users import users

import models

from flask_cors import CORS

from flask_login import LoginManager

import os

from dotenv import load_dotenv

load_dotenv()

DEBUG=True
PORT=8002

app = Flask(__name__)

app.secret_key = os.environ.get("FLASK_APP_SECRET")
print(os.environ.get("FLASK_APP_SECRET"))

login_manager = LoginManager()

login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return models.User.get(models.User.id==user_id)



CORS(pmt, origins=['http://localhost:3000'], supports_credentials=True)
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(pmt, url_prefix='/api/v1/pmt')
app.register_blueprint(users, url_prefix='/api/v1/users')



if __name__=='__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
