import connexion
import six

from apitax.api.models.auth_response import AuthResponse  # noqa: E501
from apitax.api.models.create import Create  # noqa: E501
from apitax.api.models.delete import Delete  # noqa: E501
from apitax.api.models.error_response import ErrorResponse  # noqa: E501
from apitax.api.models.response import Response  # noqa: E501
from apitax.api.models.save import Save  # noqa: E501
from apitax.api.models.user_auth import UserAuth  # noqa: E501
from apitax.api import util

from apitax.authentication.ApitaxAuthentication import ApitaxAuthentication
from apitax.api.utilities.Mappers import mapUserAuthToCredentials, mapUserToUser
from apitaxcore.models.User import User

from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from apitaxcore.drivers.Driver import Driver
from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse
from apitax.api.utilities.Lifecycle import redirectIfUnauthorized, errorIfUnauthorized
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt, get_jwt_claims)


def authenticate(user=None):  # noqa: E501
    """Authenticate

    Authenticate with the API # noqa: E501

    :param user: The user authentication object.
    :type user: dict | bytes

    :rtype: AuthResponse
    """
    if connexion.request.is_json:
        user = UserAuth.from_dict(connexion.request.get_json())  # noqa: E501

    credentials = mapUserAuthToCredentials(user)
    auth = ApitaxAuthentication.login(credentials)

    if not auth:
        return ErrorResponse(status=401, message="Invalid credentials")

    access_token = create_access_token(identity={'username': user.username, 'role': auth['role']})
    refresh_token = create_refresh_token(identity={'username': user.username, 'role': auth['role']})

    return AuthResponse(status=201, message='User ' + user.username + ' was authenticated as ' + auth['role'],
                        access_token=access_token, refresh_token=refresh_token,
                        auth=UserAuth(username=auth['credentials'].username, api_token=auth['credentials'].token))


@jwt_required
def create_user(user, name, create=None):  # noqa: E501
    """Create a new script

    Create a new script # noqa: E501

    :param user: Get user with this name
    :type user: str
    :param name: Get status of a driver with this name
    :type name: str
    :param create: The data needed to create this user
    :type create: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        create = Create.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    user: User = mapUserToUser(create.script)

    if driver.createApitaxUser(user):
        return Response(status=200, body=response.getResponseBody())

    return ErrorResponse(status=500, message='Failed to create user')


@jwt_required
def delete_user(user, name, delete=None):  # noqa: E501
    """Delete a script

    Delete a script # noqa: E501

    :param user: Get user with this name
    :type user: str
    :param name: Get status of a driver with this name
    :type name: str
    :param delete: The data needed to delete this user
    :type delete: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        delete = Delete.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)

    if driver.deleteApitaxUser(User(username=user)):
        return Response(status=200, body=response.getResponseBody())

    return ErrorResponse(status=500, message='Failed to create user')


@jwt_required
def get_config():  # noqa: E501
    """Retrieve the config

    Retrieve the config # noqa: E501


    :rtype: Response
    """
    return 'do some magic!'


@jwt_required
def get_log(log):  # noqa: E501
    """Retrieve the logs

    Retrieve the logs # noqa: E501

    :param log: Get this log
    :type log: str

    :rtype: Response
    """
    # TODO: Implement
    return 'do some magic!'


@jwt_required
def get_user(user, name):  # noqa: E501
    """Retrieve a user

    Retrieve a user # noqa: E501

    :param user: Get user with this name
    :type user: str
    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    user: User = driver.getApitaxUser(User(username=user))
    response.body.add({'user': {'username': user.username, 'role': user.role}})

    return Response(status=200, body=response.getResponseBody())


@jwt_required
def get_user_list(name):  # noqa: E501
    """Retrieve a list of users

    Retrieve a list of users # noqa: E501

    :param name: Get status of a driver with this name
    :type name: str

    :rtype: Response
    """
    # TODO: This requires an additional driver function
    return 'do some magic!'


@jwt_refresh_token_required
def refresh_token():  # noqa: E501
    """Refreshes login token using refresh token

    Refreshes login token using refresh token # noqa: E501


    :rtype: UserAuth
    """
    current_user = get_jwt_identity()
    if not current_user:
        return ErrorResponse(status=401, message="Not logged in")
    access_token = create_access_token(identity=current_user)
    return AuthResponse(status=201, message='Refreshed Access Token', access_token=access_token, auth=UserAuth())


@jwt_required
def save_user(user, name, save=None):  # noqa: E501
    """Save a script

    Save a script # noqa: E501

    :param user: Get user with this name
    :type user: str
    :param name: Get status of a driver with this name
    :type name: str
    :param save: The data needed to save this user
    :type save: dict | bytes

    :rtype: Response
    """
    if connexion.request.is_json:
        save = Save.from_dict(connexion.request.get_json())  # noqa: E501

    response = errorIfUnauthorized(role='admin')
    if response:
        return response
    else:
        response = ApitaxResponse()

    driver: Driver = LoadedDrivers.getDriver(name)
    user: User = mapUserToUser(save.script)

    if driver.saveApitaxUser(user):
        return Response(status=200, body=response.getResponseBody())

    return ErrorResponse(status=500, message='Failed to create user')


@jwt_required
def system_status():  # noqa: E501
    """Retrieve the system status

    Retrieve the system status # noqa: E501


    :rtype: Response
    """
    # TODO: Implement
    # Return log config, security config, apitax config, IP, port, loaded drivers and used drivers
    # Return primary driver, auth driver etc.
    # Return statistics
    return 'do some magic!'
