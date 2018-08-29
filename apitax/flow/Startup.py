# System imports
import json
from time import time

# Application imports
from apitax.ah.flow.Connector import Connector

from apitax.grammar.grammartest import GrammarTest
from apitax.utilities.Numbers import round2str
from apitax.utilities.Npm import Npm

from apitax.ah.models.Credentials import Credentials

from apitax.ah.models.State import State


def serialize(obj):
    return obj.serialize()


class Startup:

    def __init__(self, usage, username, password, watcher, build, script) -> None:
        super().__init__()
        self.command = ""
        self.t0 = time()
        self.log = State.log
        self.config = State.config
        self.options = State.options

        self.usage = usage
        self.username = username
        self.password = password
        self.watcher = watcher
        self.build = build
        self.script = script

    def execute(self, command):
        self.command = command

        if (self.usage == 'cli'):
            # Authentication is incorporated into Connector

            if (self.options.debug):
                self.log.log(">>> Starting Processing")
                self.log.log("")
                self.log.log("")

            self.connector = Connector(options=self.options, command=self.command,
                                       credentials=Credentials(username=self.username, password=self.password),
                                       json=True)
            self.result = self.connector.execute()

            # print(str(connector.http.getCatalog()))

            if (self.options.debug):
                self.log.log(">>> Finished Processing")
                self.log.log("")
                self.log.log("")

            if (self.options.debug and self.command.split(' ')[0] == 'script'):
                for t in self.result.getRequest().parser.threads:
                    t.join()
                self.log.log(">> Dumping Current DataStore Status:")
                self.log.log("")
                self.log.log("")
                self.log.log(json.dumps(self.result.getRequest().parser.data.getStatus(), default=serialize))
                self.log.log("")
                self.log.log("")
            # print(result.getRequest().data.getData('5.3.role_assignments.0.links.assignment'))

            if (self.options.debug):
                self.log.log(">> Apitax finished processing in " + round2str(time() - self.t0) + "s")
                self.log.log("")
                self.log.log("")

        elif (self.usage == 'api'):
            from apitax.ah.api.Server import startDevServer
            self.log.log(">> Booting Up API Server:")
            self.log.log("")
            self.server = startDevServer(self.config.get("ip"), self.config.get("port"))

        elif (self.usage == 'grammar-test'):
            GrammarTest(self.script)

        elif (self.usage == 'feature-test'):
            pass

        else:
            self.log.log("### Error: Unknown mode")

        self.log.getLoggerDriver().outputLog()

        # print(">> Apitax finished processing in {0:.2f}s".format(t1 - t0))
