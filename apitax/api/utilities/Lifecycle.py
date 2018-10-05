from apitaxcore.models.State import State
from apitax.api.utilities.Roles import hasAccess as roleAccess

from apitax.api.models.error_response import ErrorResponse

from flask import redirect
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)


def hasAccess(role='admin'):
    if (roleAccess(get_jwt_identity(), role)):
        return True
    return False

def errorIfUnauthorized(role='admin', message='Your role does not allow you access to this'):
    if not hasAccess(role):
        return ErrorResponse(status=401, message=message)
    return False

def redirectIfUnauthorized(role='admin', page="login", code=303):
    if not hasAccess(role):
        return redirect(State.baseUrl + page, code=code)
    return False
