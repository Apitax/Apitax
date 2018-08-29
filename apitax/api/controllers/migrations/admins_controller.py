import connexion
import six

from apitax.ah.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.ah.api.models.response import Response  # noqa: E501
from apitax.ah.api import util


def display_admin_dashboard():  # noqa: E501
    """Displays the developer admin page

    Displays the user admin page # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def driver_status(name):  # noqa: E501
    """Retrieve the status of a loaded driver

    Retrieve the status of a loaded driver # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    return 'do some magic!'


def system_status():  # noqa: E501
    """Retrieve the system status

    Retrieve the system status # noqa: E501


    :rtype: Response
    """
    return 'do some magic!'
