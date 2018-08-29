import connexion
import six

from apitax.ah.api.models.create import Create  # noqa: E501
from apitax.ah.api.models.delete import Delete  # noqa: E501
from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.rename import Rename  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.models.save import Save  # noqa: E501
from apitax.ah.api import util


def create_script(create=None):  # noqa: E501
    """Create a new script

    Create a new script # noqa: E501

    :param create: The data needed to create this script
    :type create: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        create = Create.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_script(delete=None):  # noqa: E501
    """Delete a script

    Delete a script # noqa: E501

    :param delete: The data needed to delete this script
    :type delete: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        delete = Delete.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def display_developer_dashboard():  # noqa: E501
    """Displays the developer dashboard page

    Displays the user dashboard page # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def rename_script(rename=None):  # noqa: E501
    """Rename a script

    Rename a script # noqa: E501

    :param rename: The data needed to save this script
    :type rename: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        rename = Rename.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def save_script(save=None):  # noqa: E501
    """Save a script

    Save a script # noqa: E501

    :param save: The data needed to save this script
    :type save: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        save = Save.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
