#!/usr/bin/env python

from apitax.ah.models.State import State

State.paths['root'] = '/app'
State.paths['config'] = '/app/config.txt'

from project import Project
project = Project()

# Setup must run before importing the 'app' object from the API Server
from apitax.ah.flow.Setup import Setup
setup = Setup()

# Put Driver imports here
from apitax.drivers.Drivers import Drivers
from apitax.drivers.builtin.Api import Api
from apitax.drivers.builtin.Scriptax import Scriptax

Drivers.add("Api", Api())
Drivers.add("Scriptax", Scriptax())

project.loadDrivers()
# End driver imports

# Put your custom logic here

# End custom logic

# These should probably be the last lines of your file
setup.load()
from apitax.ah.api.Server import *

# Uncomment to debug without uwsgi or nginx
app.run(port=5085, host='0.0.0.0')
