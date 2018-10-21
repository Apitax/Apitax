import connexion
import six

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.execute import Execute  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api import util

from apitaxcore.models.State import State
from apitaxcore.models.Credentials import Credentials
from apitaxcore.models.Options import Options
from commandtax.flow.Connector import Connector
from apitax.api.utilities.Mappers import mapUserAuthToCredentials

import traceback

from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.api.utilities.Lifecycle import redirectIfUnauthorized, errorIfUnauthorized
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)


@jwt_required
def command(driver, execute=None):  # noqa: E501
    """Execute a Command

    Execute a command # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param execute: The data needed to execute this command
    :type execute: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        execute = Execute.from_dict(connexion.request.get_json())  # noqa: E501

    # TODO: Utilize the driver passed rather than the first string component

    response = errorIfUnauthorized(role='admin')
    if response:
        return response

    try:
        parameters = {}

        if execute.command.parameters:
            parameters = execute.command.parameters

        credentials = Credentials()

        options = Options()

        if execute.command.options:
            if 'debug' in execute.command.options:
                options.debug = execute.command.options['debug']

            if 'sensitive' in execute.command.options:
                options.sensitive = execute.command.options['sensitive']

        if execute.auth:
            credentials = mapUserAuthToCredentials(execute.auth, credentials)
            if not execute.auth.api_token:
                options.sensitive = True

        connector = Connector(options=options, credentials=credentials, command=execute.command.command,
                              parameters=parameters)

        response: ApitaxResponse = connector.execute()

        response = Response(status=response.getResponseStatusCode(), body=response.getResponseBody())

        if options.debug:
            response.log = connector.logBuffer

        return response
    except:
        State.log.error(traceback.format_exc())
        if 'debug' in execute.command.options and execute.command.options['debug']:
            return ErrorResponse(status=500,
                                 message="Uncaught exception occured during processing. To get a larger stack trace, visit the logs.",
                                 state=traceback.format_exc(3))
        else:
            return ErrorResponse(status=500, message="")
