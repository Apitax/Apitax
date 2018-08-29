from apitax.ah.models.State import State
# from apitax.ah.commandtax.ApiAuthentication import AuthRequest
from apitax.ah.flow.LoadedDrivers import LoadedDrivers
from apitax.ah.models.Credentials import Credentials
from apitax.drivers.Driver import Driver
from apitax.ah.flow.responses.ApitaxResponse import ApitaxResponse
import base64


class ApitaxAuthentication:

    @staticmethod
    def getBasicHttp(credentials: Credentials):
        temp = credentials.username + ':' + credentials.password
        return {'Authorization': 'Basic ' + base64.b64encode(temp.encode('utf-8'))}

    @staticmethod
    def getBearerHttp(credentials: Credentials):
        return {'Authorization': 'Bearer ' + credentials.token}

    @staticmethod
    def login(credentials):
        driver: Driver = LoadedDrivers.getAuthDriver()
        role = None
        if(not driver.isDriverAuthenticatable()):
            return None
        if (driver.isApitaxAuthBasedOnApiAuth()):
            # apiDriver = LoadedDrivers.getPrimaryDriver()
            apiDriver: Driver = driver

            if ('driver' in credentials.extra):
                apiDriver = LoadedDrivers.getDriver(credentials.extra['driver'])
            result: ApitaxResponse = apiDriver.authenticateApi(credentials)

            if (not result.isStatusSuccess()):
                return None

            role = driver.authenticateApitax(result.getResponseBody()['credentials'])
            if (apiDriver.isApiTokenable()):
                credentials.token = apiDriver.getApiToken(result)
        else:
            role = driver.authenticateApitax(credentials)

        if (not role):
            return None
        return {"role": role, "credentials": credentials}
