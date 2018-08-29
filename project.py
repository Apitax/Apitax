from apitax.ah.models.State import State
from apitax.utilities.Files import getPath
from apitax.drivers.Drivers import Drivers


class Project:
    def __init__(self):
        State.paths['root'] = getPath('.')
        State.paths['config'] = getPath('config.txt')

    def loadDrivers(self):
        from apitax.drivers.builtin.BasicAuth import BasicAuth
        Drivers.add("BasicAuth", BasicAuth())

