
from apitaxcore.models.Credentials import Credentials
from apitax.api.models.user_auth import UserAuth


def mapUserAuthToCredentials(userAuth: UserAuth, credentials=Credentials()):
    if (userAuth.api_token):
        credentials.token = userAuth.api_token
    else:
        credentials.username = userAuth.username
        credentials.password = userAuth.password

    if (userAuth.extra):
        credentials.extra = userAuth.extra

    return credentials

