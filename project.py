from apitaxcore.drivers.Drivers import Drivers


class Project:
    def loadDrivers(self):
        from apitaxdrivers.Github import GithubDriver
        Drivers.add("github", GithubDriver())
        #from apitax.drivers.builtin.BasicAuth import BasicAuth
        #Drivers.add("BasicAuth", BasicAuth())

