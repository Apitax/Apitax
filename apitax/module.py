# Apitax
# Originally created by Shawn Clake
# shawn.clake@gmail.com
# May 2018
#
# Contains Scriptax and Commandtax
#
# This application is used to automate API processes using arbitrary API's
# It includes a CLI as well as web interface
# However the web interface will need to be customized per API usage

from apitax.ah.flow.Setup import Setup
from apitax.ah.flow.Startup import Startup


class Apitax:

    # Entry point of the program
    def __init__(self, args: list):
        # General procedure is as follows
        # Sets up logical defaults for parameters
        # Checks config for any overrides to those params
        # Checks cli params for any overrides to those params
        # CLI > Config > Default
        setup = Setup(args).load()
        startup = Startup(setup.usage, setup.username, setup.password, setup.watcher, setup.build, setup.script)
        startup.execute(setup.command)


