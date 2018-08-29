from apitax.ah.models.Credentials import Credentials
from apitax.drivers.Driver import Driver
from apitax.utilities.Json import read
from apitax.ah.models.State import State
from apitax.utilities.Files import getPath


class BasicAuth(Driver):
    def __init__(self):
        super().__init__()
        self.users = read(getPath(State.paths['root'] + "/app/users.json"))

    def getDriverName(self) -> str:
        return "Basic Auth"

    def getDriverDescription(self) -> str:
        return "Provides out of the box authentication"

    def getDriverHelpEndpoint(self) -> str:
        return "coming soon"

    def getDriverTips(self) -> str:
        return "coming soon"

    def isDriverAuthenticatable(self) -> bool:
        return True

    def isApitaxAuthBasedOnApiAuth(self) -> bool:
        return False

    def authenticateApitax(self, credentials: Credentials = None) -> str:
        try:
            if (credentials.password == self.users[credentials.username]['password']):
                return self.users[credentials.username]['role']
        except:
            return None
        return None