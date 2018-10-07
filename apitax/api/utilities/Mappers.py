
from apitaxcore.models.Credentials import Credentials
from apitaxcore.models.User import User
from apitax.api.models.user_auth import UserAuth
from apitax.api.models.user import User as UserModel


def mapUserAuthToCredentials(userAuth: UserAuth, credentials=None):
    if not credentials:
        credentials = Credentials()

    if userAuth.api_token:
        credentials.token = userAuth.api_token
    else:
        credentials.username = userAuth.username
        credentials.password = userAuth.password

    if userAuth.extra:
        credentials.extra = userAuth.extra

    return credentials


def mapUserToUser(userModel: UserModel, user: User = None):
    if not user:
        user = User()

    if userModel.username:
        user.username = userModel.username

    if userModel.password:
        user.password = userModel.password

    if userModel.role:
        user.role = userModel.role

    return user

