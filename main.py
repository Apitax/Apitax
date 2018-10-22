#!/usr/bin/env python

"""
This file is the loading process for Apitax

Setup your app with Apitax:
* Modify /app/Project.py to represent your project
* Copy /app/config.example.txt to /app/config.txt and make changes as necessary
* Copy /app/users.example.json to /app/users.json and make changes as necessary
* Add any additional files you want to use to /app
* Feel free to install additional drivers using pip and loading them via project.py
"""

# Importing app State model to setup initial pathing
from apitaxcore.models.State import State

# Setting up default paths - Assumes docker container
State.paths['root'] = '/app'  # just /app for docker
State.paths['config'] = State.paths['root'] + '/app/config.txt'

# Sets up project and runs setup to alter any paths as necessary
from app.Project import Project
project = Project()
project.setup()

# Running Setup to initialize a bunch of models before running
from apitax.flow.Setup import Setup
args = []
if project.isDebug():
    args.append('--debug')
setup = Setup(passedArgs=args)

# Preparing Drivers
from apitaxcore.drivers.Drivers import Drivers
from apitaxcore.flow.LoadedDrivers import LoadedDrivers

# Importing core drivers
from commandtax.drivers.builtin.Commandtax import Commandtax
from scriptax.drivers.builtin.Scriptax import Scriptax
from scriptaxstd.drivers.builtin.StandardLibrary import StandardLibrary
from scriptaxstd.drivers.builtin.Api import Api
from scriptaxstd.drivers.builtin.ApiXml import ApiXml
from apitax.drivers.builtin.BasicAuth import BasicAuth
from apitax.drivers.builtin.Apitax import Apitax

# Adding imported drivers into app
Drivers.add("commandtax", Commandtax())
Drivers.add("scriptax", Scriptax())
Drivers.add("std", StandardLibrary())
Drivers.add("api", Api())
Drivers.add("api-xml", ApiXml())
Drivers.add("basic-auth", BasicAuth())
Drivers.add("apitax", Apitax())

# Loading added drivers
LoadedDrivers.load("commandtax")
LoadedDrivers.load("scriptax")
LoadedDrivers.load("std")
LoadedDrivers.load("api")
LoadedDrivers.load("api-xml")
LoadedDrivers.load("basic-auth")
LoadedDrivers.load("apitax")

# Importing/Adding custom project drivers
project.loadDrivers()

# Finishes loading app by loading custom drivers as specified in the config
setup.load()

# If debug environment, runs flask dev server without Nginx or uWSGI
# Otherwise, tell uWSGI that main.py is the entry point
if project.isDev():
    from apitax.api.Server import *
    app.run(port=5085, host='0.0.0.0')
