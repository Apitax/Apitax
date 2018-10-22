class Project:
    def isDev(self):
        return True

    def isDebug(self):
        return True

    def setup(self):
        from apitaxcore.models.State import State
        #State.paths['root'] = 'D:/Programming/Projects/Apitax/Apitax'  # just /app for docker
        #State.paths['config'] = State.paths['root'] + '/config.txt'
        #State.paths['log'] = None

    def loadDrivers(self):
        from apitaxcore.drivers.Drivers import Drivers
        #from apitaxdrivers.Github import GithubDriver
        #Drivers.add("github", GithubDriver())
