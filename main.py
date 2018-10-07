#!/usr/bin/env python

from apitaxcore.models.State import State

# Assuming Apitax Docker Container
State.paths['root'] = 'D:/Programming/Projects/Apitax/Apitax' # just /app for docker
State.paths['config'] = State.paths['root'] + '/config.txt'

from project import Project

project = Project()

# Setup must run before importing the 'app' object from the API Server
from apitax.flow.Setup import Setup

setup = Setup(passedArgs=['--debug'])

# Put Driver imports here
from apitaxcore.drivers.Drivers import Drivers
from apitaxcore.flow.LoadedDrivers import LoadedDrivers

from commandtax.drivers.builtin.Commandtax import Commandtax
from scriptax.drivers.builtin.Scriptax import Scriptax
from scriptaxstd.drivers.builtin.StandardLibrary import StandardLibrary
from scriptaxstd.drivers.builtin.Api import Api
from scriptaxstd.drivers.builtin.ApiXml import ApiXml
from apitax.drivers.builtin.BasicAuth import BasicAuth
from apitax.drivers.builtin.Apitax import Apitax

Drivers.add("commandtax", Commandtax())
Drivers.add("scriptax", Scriptax())
Drivers.add("std", StandardLibrary())
Drivers.add("api", Api())
Drivers.add("api-xml", ApiXml())
Drivers.add("basic-auth", BasicAuth())
Drivers.add("apitax", Apitax())

LoadedDrivers.load("commandtax")
LoadedDrivers.load("scriptax")
LoadedDrivers.load("std")
LoadedDrivers.load("api")
LoadedDrivers.load("api-xml")
LoadedDrivers.load("basic-auth")
LoadedDrivers.load("apitax")

project.loadDrivers()

# These should probably be the last lines of your file
setup.load()
from apitax.api.Server import *

# Uncomment to debug without uwsgi or nginx
app.run(port=5085, host='0.0.0.0')
