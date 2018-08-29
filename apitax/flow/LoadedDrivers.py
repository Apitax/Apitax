from apitax.drivers.Drivers import Drivers
from apitax.logs.Log import Log
from apitax.ah.models.State import State


class LoadedDrivers:
    drivers = {}

    default = {}

    @staticmethod
    def load(name):
        setDefaultDrivers = False
        if (not LoadedDrivers.default):
            setDefaultDrivers = True

        name = (name + 'driver').lower()

        if (name not in Drivers.drivers):
            Log().error("Driver '" + name + "' does not exist or has not been imported/added.")
        else:
            LoadedDrivers.drivers[name] = Drivers.get(name)

            if (setDefaultDrivers):
                LoadedDrivers.default['base'] = Drivers.get(name)

            Log().log("> Driver '" + name + "' is loaded.")
            Log().log('')

    @staticmethod
    def getDefaultDriver():
        return LoadedDrivers.default['base']

    @staticmethod
    def getPrimaryDriver():
        if (not State.config.has("drivers-primary") or State.config.get("drivers-primary") == "default"):
            return LoadedDrivers.getDefaultDriver()
        return LoadedDrivers.getDriver((State.config.get('drivers-primary')).lower())

    @staticmethod
    def getAuthDriver():
        if (not State.config.has("drivers-auth") or State.config.get("drivers-auth") == "default"):
            return LoadedDrivers.getDefaultDriver()
        return LoadedDrivers.getDriver((State.config.get('drivers-auth')).lower())

    @staticmethod
    def getDriver(name):
        name = (name + 'driver').lower()
        if (name not in Drivers.drivers):
            Log().error("Driver '" + name + "' has not been loaded.")
            return None
        return LoadedDrivers.drivers[name]
