#!/usr/bin/env python

import connexion

from apitax.api import encoder
from flask_jwt_extended import JWTManager

from apitaxcore.models.State import State

from flask import redirect, Response

app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Apitax'})

app.app.config['JWT_SECRET_KEY'] = State.config.get("secret") # More config here: http://flask-jwt-extended.readthedocs.io/en/latest/options.html#configuration-options
jwt = JWTManager(app.app)

if State.config.get('allow-cors'):
    from flask_cors import CORS
    CORS(app.app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'username': identity['username'],
        'role': identity['role']
    }


@jwt.unauthorized_loader
def unauthorized_loader(): # More types here: http://flask-jwt-extended.readthedocs.io/en/latest/changing_default_behavior.html
    return Response(status=401, response='You must login')


@jwt.invalid_token_loader
def invalid_token_loader(): # More types here: http://flask-jwt-extended.readthedocs.io/en/latest/changing_default_behavior.html
    return Response(status=401, response='You must login')


@jwt.expired_token_loader
def expired_token_loader(): # More types here: http://flask-jwt-extended.readthedocs.io/en/latest/changing_default_behavior.html
    return Response(status=401, response='You must login')


def redirectUnauthorized(page="login", code=303):
    return redirect(State.baseUrl + page, code=code)


def startDevServer(ip, port):
    app.run(port=port, host=ip, debug=False)
