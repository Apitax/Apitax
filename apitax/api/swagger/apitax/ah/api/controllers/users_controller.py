import connexion
import six

from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.execute import Execute  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api.models.user_auth import UserAuth  # noqa: E501
from apitax.ah.api import util


def command(execute=None):  # noqa: E501
    """Execute a Command

    Execute a command # noqa: E501

    :param execute: The data needed to execute this command
    :type execute: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        execute = Execute.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def display_dashboard():  # noqa: E501
    """Displays the user dashboard page

    Displays the user dashboard page # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def endpoint_catalog(catalog=None):  # noqa: E501
    """Retrieve the endpoint catalog

    Retrieve the endpoint catalog # noqa: E501

    :param catalog: The data needed to get a catalog
    :type catalog: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        catalog = UserAuth.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_script(name=None):  # noqa: E501
    """Retrieve the contents of a script

    Retrieve the contents of a script # noqa: E501

    :param name: The script name.
    :type name: str

    :rtype: Response
    """
    return 'do some magic!'


def script_catalog():  # noqa: E501
    """Retrieve the script catalog

    Retrieve the script catalog # noqa: E501


    :rtype: Response
    """
    return 'do some magic!'
