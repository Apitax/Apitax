import connexion
import six

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api import util

from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from apitaxcore.drivers.Driver import Driver
from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.api.utilities.Lifecycle import redirectIfUnauthorized, errorIfUnauthorized
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)

@jwt_required
def get_driver_api_catalog(name):  # noqa: E501
    """Retrieve the api catalog

    Retrieve the api catalog # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    response.body.add(driver.getApiEndpointCatalog())

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def get_driver_api_status(name):  # noqa: E501
    """Retrieve the status of an api

    Retrieve the status of an api # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    response.body.add({"format": driver.getApiFormat()})
    response.body.add({"description": driver.getApiDescription()})
    response.body.add({"status": driver.getApiStatus()})
    response.body.add({"auth-type": driver.getApiAuthType()})

    endpoints = {}
    endpoints['base'] = driver.getApiBaseEndpoint()
    endpoints['catalog'] = driver.getApiCatalogEndpoint()
    endpoints['auth'] = driver.getApiAuthEndpoint()
    response.body.add({'endpoints': endpoints})

    options = {}
    options['authenticatable'] = driver.isApiAuthenticated()
    options['authentication-separate'] = driver.isApiAuthenticationSeparateRequest()
    options['cataloggable'] = driver.isApiCataloggable()
    options['tokenable'] = driver.isApiTokenable()
    response.body.add({'options': options})

    return Response(status=200, body=response.getResponseBody())
