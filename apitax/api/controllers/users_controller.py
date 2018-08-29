import json
import traceback

import connexion
import six

import flask

from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.execute import Execute  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.models.user_auth import UserAuth  # noqa: E501
from apitax.ah.api import util

from apitax.ah.models.State import State
from apitax.ah.flow.LoadedDrivers import LoadedDrivers
from apitax.ah.models.Credentials import Credentials
from apitax.ah.models.Options import Options
from apitax.ah.flow.Connector import Connector
from apitax.ah.api.utilities.Mappers import mapUserAuthToCredentials

from apitax.ah.api.utilities.Roles import hasAccess as roleAccess
from flask import redirect

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)


@jwt_required
def command(execute=None):  # noqa: E501
    """Execute a Command

    Execute a command # noqa: E501

    :param execute: The data needed to execute this command
    :type execute: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        execute = Execute.from_dict(connexion.request.get_json())  # noqa: E501

    if (not hasAccess()):
        return redirectUnauthorized()

    try:
        connector = None

        parameters = {}

        if (execute.command.parameters):
            parameters = execute.command.parameters

        credentials = Credentials()

        options = Options()

        if(execute.command.options):
            if ('debug' in execute.command.options):
                options.debug = execute.command.options['debug']

            if ('sensitive' in execute.command.options):
                options.sensitive = execute.command.options['sensitive']

        if (execute.auth):
            credentials = mapUserAuthToCredentials(execute.auth, credentials)
            if (not execute.auth.api_token):
                options.sensitive = True

        connector = Connector(options=options, credentials=credentials, command=execute.command.command,
                              parameters=parameters)

        commandHandler = connector.execute()

        response = Response(status=commandHandler.response.getResponseStatusCode(),
                            body=commandHandler.response.getResponseBody())

        if(options.debug):
            response.log = connector.logBuffer

        return response
    except:
        State.log.error(traceback.format_exc())
        if ('debug' in execute.command.options and execute.command.options['debug']):
            return ErrorResponse(status=500,
                                 message="Uncaught exception occured during processing. To get a larger stack trace, visit the logs.",
                                 state=traceback.format_exc(3))
        else:
            return ErrorResponse(status=500, message="")


# @jwt_required
def display_dashboard():  # noqa: E501
    """Displays the user dashboard page

    Displays the user dashboard page # noqa: E501


    :rtype: None
    """

    #   if(not hasAccess()):
    #      return redirectUnauthorized()

    return flask.send_from_directory('dashboard/src/pages', 'user_dashboard.html')


@jwt_required
def endpoint_catalog(catalog=None):  # noqa: E501
    """Retrieve the endpoint catalog

    Retrieve the endpoint catalog # noqa: E501

    :param catalog: The data needed to get a catalog
    :type catalog: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        catalog = UserAuth.from_dict(connexion.request.get_json())  # noqa: E501

    if (not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    auth = None
    if (catalog):
        auth = catalog
    return Response(status=200, body=driver.getCatalog(auth))


@jwt_required
def get_script(name=None):  # noqa: E501
    """Retrieve the contents of a script

    Retrieve the contents of a script # noqa: E501

    :param name: The script name.
    :type name: str

    :rtype: Response
    """

    if (not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    return Response(status=200, body=driver.readScript(name))


@jwt_required
def script_catalog():  # noqa: E501
    """Retrieve the script catalog

    Retrieve the script catalog # noqa: E501


    :rtype: Response
    """
    if (not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    return Response(status=200, body=driver.getScriptsCatalog())


def hasAccess():
    if (roleAccess(get_jwt_identity(), 'user')):
        return True
    return False


def redirectUnauthorized(page="login", code=303):
    return redirect(State.baseUrl + page, code=code)
