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
def get_driver_blacklist(driver):  # noqa: E501
    """Retrieve the blacklist in the driver

    Retrieve the blacklist in the driver # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    response.body.add({'blacklist': driver.getDriverBlacklist()})

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_config(driver):  # noqa: E501
    """Retrieve the config of a loaded driver

    Retrieve the config of a loaded driver # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    # TODO: This needs an implementation, but likely requires a change to configs in apitaxcore

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_list():  # noqa: E501
    """Retrieve the catalog of drivers

    Retrieve the catalog of drivers # noqa: E501


    :rtype: Response
    """

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    response.body.add({'drivers': LoadedDrivers.drivers})

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_status(driver):  # noqa: E501
    """Retrieve the status of a loaded driver

    Retrieve the status of a loaded driver # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    response.body.add({'name': driver.getDriverName()})
    response.body.add({'description': driver.getDriverDescription()})
    response.body.add({'tips': driver.getDriverTips()})
    response.body.add({'help': driver.getDriverHelpEndpoint()})
    response.body.add({'minimum-role': driver.getDriverMinimumRole()})

    options = {}
    options['configurable'] = driver.isDriverConfigurable()
    options['authenticatable'] = driver.isDriverAuthenticatable()
    options['role-restricted'] = driver.isDriverRoleRestricted()
    options['whitelisted'] = driver.isDriverWhitelisted()
    options['blacklisted'] = driver.isDriverBlacklisted()
    response.body.add({'options': options})

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_whitelist(driver):  # noqa: E501
    """Retrieve the whitelist in the driver

    Retrieve the whitelist in the driver # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    response.body.add({'whitelist': driver.getDriverWhitelist()})

    return Response(status=200, body=response.getResponseBody())
