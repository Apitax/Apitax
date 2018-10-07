import connexion
import six

from apitax.api.models.create1 import Create1  # noqa: E501
from apitax.api.models.delete1 import Delete1  # noqa: E501
from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.rename import Rename  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.save1 import Save1  # noqa: E501
from apitax.api import util

from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from scriptax.drivers.Driver import Driver
from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.api.utilities.Lifecycle import redirectIfUnauthorized, errorIfUnauthorized
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)

@jwt_required
def create_driver_script(name, create=None):  # noqa: E501
    """Create a new script

    Create a new script # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str
    :param create: The data needed to create this script
    :type create: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        create = Create1.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    driver.saveDriverScript(create.script.name, create.script.content)

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def delete_driver_script(name, delete=None):  # noqa: E501
    """Delete a script

    Delete a script # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str
    :param delete: The data needed to delete this script
    :type delete: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        delete = Delete1.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    driver.deleteDriverScript(delete.script.name)

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def get_driver_script(name2, name=None):  # noqa: E501
    """Retrieve the contents of a script

    Retrieve the contents of a script # noqa: E501

    :param name2: Get status of a driver with this name
    :type name2: str
    :param name: The script name.
    :type name: str

    :rtype: Response
    """
    response = errorIfUnauthorized(role='user')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name2)

    response.body.add({'content': driver.getDriverScript(name)})

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def get_driver_script_catalog(name):  # noqa: E501
    """Retrieve the script catalog

    Retrieve the script catalog # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='user')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)

    response.body.add(driver.getDriverScriptCatalog().get())

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def rename_driver_script(name, rename=None):  # noqa: E501
    """Rename a script

    Rename a script # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str
    :param rename: The data needed to save this script
    :type rename: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        rename = Rename.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    if not driver.renameDriverScript(rename.original.name, rename.new.name):
        return ErrorResponse(status=500, message='Cannot rename to an existing file.')

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def save_driver_script(name, save=None):  # noqa: E501
    """Save a script

    Save a script # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str
    :param save: The data needed to save this script
    :type save: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        save = Save1.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    driver.saveDriverScript(save.script.name, save.script.content)

    return Response(status=200, body=response.getResponseBody())
