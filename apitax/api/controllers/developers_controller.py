import connexion
import six

from apitax.ah.api.models.create import Create  # noqa: E501
from apitax.ah.api.models.delete import Delete  # noqa: E501
from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.rename import Rename  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.models.save import Save  # noqa: E501
from apitax.ah.api import util

from apitax.ah.models.State import State
from apitax.ah.flow.LoadedDrivers import LoadedDrivers
from apitax.ah.api.utilities.Roles import isRole

from apitax.ah.api.utilities.Roles import hasAccess as roleAccess
from flask import redirect

from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)

@jwt_required
def create_script(create=None):  # noqa: E501
    """Create a new script

    Create a new script # noqa: E501

    :param Scripts: The data needed to create this script
    :type Scripts: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        create = Create.from_dict(connexion.request.get_json())  # noqa: E501

    if(not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    driver.saveScript(create.script.name, create.script.content)
    return Response(status=200, body={'file-name': create.script.name})


@jwt_required
def delete_script(delete=None):  # noqa: E501
    """Delete a script

    Delete a script # noqa: E501

    :param delete: The data needed to delete this script
    :type delete: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        delete = Delete.from_dict(connexion.request.get_json())  # noqa: E501

    if(not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    driver.deleteScript(delete.script.name)
    return Response(status=200, body={})


@jwt_required
def display_developer_dashboard():  # noqa: E501
    """Displays the developer dashboard page

    Displays the user dashboard page # noqa: E501


    :rtype: None
    """

    if(not hasAccess()):
        return redirectUnauthorized()

    return 'do some magic!'


@jwt_required
def rename_script(rename=None):  # noqa: E501
    """Rename a script

    Rename a script # noqa: E501

    :param rename: The data needed to save this script
    :type rename: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        rename = Rename.from_dict(connexion.request.get_json())  # noqa: E501

    if(not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    if (not driver.renameScript(rename.original.name, rename.new.name)):
        return ErrorResponse(status=500, message='Cannot rename to an existing file.')
    return Response(status=200, body={'file-name': rename.new.name})


@jwt_required
def save_script(save=None):  # noqa: E501
    """Save a script

    Save a script # noqa: E501

    :param Scripts: The data needed to save this script
    :type Scripts: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        save = Save.from_dict(connexion.request.get_json())  # noqa: E501

    if(not hasAccess()):
        return redirectUnauthorized()

    driver = LoadedDrivers.getDefaultDriver()
    driver.saveScript(save.script.name, save.script.content)
    return Response(status=200, body={'file-name': save.script.name})

def hasAccess():
    if (roleAccess(get_jwt_identity(), 'developer')):
        return True
    return False


def redirectUnauthorized(page="login", code=303):
    return redirect(State.baseUrl + page, code=code)
