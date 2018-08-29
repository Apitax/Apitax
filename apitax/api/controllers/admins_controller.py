import connexion
import six

from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api import util

from apitax.ah.models.State import State
from apitax.ah.flow.LoadedDrivers import LoadedDrivers

from apitax.ah.api.utilities.Roles import hasAccess as roleAccess
from flask import redirect

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)


@jwt_required
def display_admin_dashboard():  # noqa: E501
    """Displays the developer admin page

    Displays the user admin page # noqa: E501


    :rtype: None
    """
    if(not hasAccess()):
        return redirectUnauthorized()

    return 'do some magic!'


@jwt_required
def driver_status(name):  # noqa: E501
    """Retrieve the status of a loaded driver

    Retrieve the status of a loaded driver # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    if(not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    body = {"name": str(driver.__class__.__name__)}
    body.update(driver.serialize())
    return Response(status=200, body=body)


@jwt_required
def system_status():  # noqa: E501
    """Retrieve the system status

    Retrieve the system status # noqa: E501


    :rtype: Response
    """
    if(not hasAccess()):
        return redirectUnauthorized()

    body = State.config.serialize(["driver", "log", "log-file", "log-colorize"])
    body.update({'debug': State.options.debug, 'sensitive': State.options.sensitive})
    return Response(status=200, body=body)


def hasAccess():
    if (roleAccess(get_jwt_identity(), 'admin')):
        return True
    return False


def redirectUnauthorized(page="login", code=303):
    return redirect(State.baseUrl + page, code=code)
