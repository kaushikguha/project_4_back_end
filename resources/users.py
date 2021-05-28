import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from playhouse.shortcuts import model_to_dict
from flask_login import login_user, logout_user

users=Blueprint('users', 'users')

@users.route('/', methods=['GET'])
def test_user_resource():
    return "user resource works"

################################# REGISTER
@users.route('/register', methods=['POST'])
def register():
    payload= request.get_json()

    # payload['email']=payload['email'].lower()
    payload['username']=payload['username'].lower()
    print (payload)

    try:
        models.User.get(models.User.username==payload['username'])
        return jsonify(
            data={},
            message="A user with that username already exists",
            status=401
        ), 401

    except models.DoesNotExist:
        pw_hash=generate_password_hash(payload['password'])

        created_user=models.User.create(
            ssn=payload['ssn'],
            first_name=payload['first_name'],
            last_name=payload['last_name'],
            email=payload['email'],
            username=payload['username'],
            password=pw_hash
        )
        print(created_user)

        login_user(created_user)



        created_user_dict=model_to_dict(created_user)
        print(created_user_dict)
        print(type(created_user_dict['password']))
        created_user_dict.pop('password')

        return jsonify(
        data=created_user_dict,
        message='successfully registered user',
        status=201
        ), 201
######################## login
@users.route('/login', methods=['POST'])
def login():
    payload=request.get_json()
    # payload['email']=payload['email'].lower()
    payload['username']=payload['username'].lower()

    try:
        user=models.User.get(models.User.username==payload['username'])

        user_dict=model_to_dict(user)
        password_is_good=check_password_hash(user_dict['password'], payload['password'])

        if (password_is_good):
            login_user(user)

            user_dict.pop('password')

            return jsonify(
                data=user_dict,
                message=f"successfully logged in {user_dict['username']}",
                status=200
            ), 200

        else:
            print('password is not good')

            return jsonify(
                data={},
                message='Email or password is incorrect',
                status=401
            ), 401

    except models.DoesNotExist:
        print('usernmame is no good')
        return jsonify(
            data={},
            message='Email or password is incorrect',
            status=401
        ), 401

#logout route
@users.route('/logout', methods=['GET'])

def logout():
    logout_user()
    return jsonify(
        data={},
        status=200,
        message='User Successfully logged out'

        )
