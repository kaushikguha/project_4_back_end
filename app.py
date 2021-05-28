
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

# @app.route('/')
# def hello():
#     return 'Hello World!'
#
# @app.route('/test')
# def get_list():
#     return ['hello', 'hi', 'hey']
#
# @app.route('/test_json')
# def get_json():
#     return jsonify(['hello', 'hi', 'hey'])
#
# @app.route('/cat_json')
# def get_cat_json():
#     return jsonify(name='princess baby cat', age=9)
#
# @app.route('/nested_json')
# def get_nested_json():
#     bebes={
#         'name': 'princess baby cat',
#         'age':9,
#         'cute':True,
#         'sweet': True
#     }
#     return jsonify(name="Matt K", age=24, cat=bebes)
#
# @app.route('/two_cats')
# def get_two_cats():
#     bebes={
#         'name': 'princess baby cat',
#         'age':9,
#         'cute':True,
#         'sweet': True
#     }
#     sir={
#         'name': 'Sir Charles III',
#         'age':5,
#         'cute':True,
#         'sweet': False
#     }
#     return jsonify(name="Matt K", age=24, cats=[bebes, sir])
#
#
# @app.route('/say_hello/<username>')
# def say_hello(username):
#     return 'Hello {}'.format(username)




if __name__=='__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)
