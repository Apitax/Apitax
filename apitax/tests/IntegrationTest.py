# Application import
from scriptax.parser.utils.BoilerPlate import customizableParser
from scriptax.drivers.builtin.Scriptax import Scriptax
from commandtax.drivers.builtin.Commandtax import Commandtax
from scriptaxstd.drivers.builtin.StandardLibrary import StandardLibrary
from scriptaxstd.drivers.builtin.Api import Api
from scriptaxstd.drivers.builtin.ApiXml import ApiXml

from apitaxcore.logs.Log import Log
from apitaxcore.logs.StandardLog import StandardLog
from apitaxcore.models.State import State
from apitaxcore.flow.LoadedDrivers import LoadedDrivers
from apitaxcore.drivers.Drivers import Drivers

State.log = Log(StandardLog(), logColorize=False)

#State.log.log("> test")

Drivers.add("commandtax", Commandtax())
Drivers.add("scriptax", Scriptax())
Drivers.add("api", Api())
Drivers.add("apixml", ApiXml())
Drivers.add("std", StandardLibrary())
LoadedDrivers.load("commandtax")
LoadedDrivers.load("scriptax")
LoadedDrivers.load("api")
LoadedDrivers.load("apixml")
LoadedDrivers.load("std")

scriptax = "from std import String as String; log(String.substr(text='this_is_some_fantastic_text', start=3, length=10));"

visitor = customizableParser(scriptax, file='inline_program')

print('Return: ' + str(visitor[0][1]))
print()
print("===")