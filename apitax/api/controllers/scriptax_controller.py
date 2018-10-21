import connexion
import six

from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.script_create import ScriptCreate  # noqa: E501
from apitax.api.models.script_delete import ScriptDelete  # noqa: E501
from apitax.api.models.script_rename import ScriptRename  # noqa: E501
from apitax.api.models.script_save import ScriptSave  # noqa: E501
from apitax.api import util

from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from scriptax.drivers.Driver import Driver
from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.api.utilities.Lifecycle import redirectIfUnauthorized, errorIfUnauthorized
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)

@jwt_required
def create_driver_script(driver, script_create=None):  # noqa: E501
    """Create a new script

    Create a new script # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param script_create: The data needed to create this script
    :type script_create: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        script_create = ScriptCreate.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    driver.saveDriverScript(script_create.script.name, script_create.script.content)

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def delete_driver_script(driver, script_delete=None):  # noqa: E501
    """Delete a script

    Delete a script # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param script_delete: The data needed to delete this script
    :type script_delete: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        script_delete = ScriptDelete.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    driver.deleteDriverScript(script_delete.script.name)

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_script(driver, script=None):  # noqa: E501
    """Retrieve the contents of a script

    Retrieve the contents of a script # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param script: The script name.
    :type script: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='user')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)

    response.body.add({'content': driver.getDriverScript(script)})

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def get_driver_script_catalog(driver):  # noqa: E501
    """Retrieve the script catalog

    Retrieve the script catalog # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str

    :rtype: Response
    """

    response = errorIfUnauthorized(role='user')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)

    response.body.add(driver.getDriverScriptCatalog().get())

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def rename_driver_script(driver, script_rename=None):  # noqa: E501
    """Rename a script

    Rename a script # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param script_rename: The data needed to rename this script
    :type script_rename: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        script_rename = ScriptRename.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    if not driver.renameDriverScript(script_rename.original.name, script_rename.new.name):
        return ErrorResponse(status=500, message='Cannot rename to an existing file.')

    return Response(status=200, body=response.getResponseBody())

@jwt_required
def save_driver_script(driver, script_save=None):  # noqa: E501
    """Save a script

    Save a script # noqa: E501

    :param driver: The driver to use for the request. ie. github
    :type driver: str
    :param script_save: The data needed to save this script
    :type script_save: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        script_save = ScriptSave.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='developer')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(driver)
    driver.saveDriverScript(script_save.script.name, script_save.script.content)

    return Response(status=200, body=response.getResponseBody())
