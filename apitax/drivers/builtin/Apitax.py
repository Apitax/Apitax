from apitaxcore.flow.responses.ApitaxResponse import ApitaxResponse

from scriptaxstd.drivers.builtin.Api import Api

from commandtax.models.Command import Command


class Apitax(Api):
    def getDriverName(self) -> str:
        return "Apitax"

    def getDriverDescription(self) -> str:
        return "Provides out of the box commandtax support for the Apitax API"

    def getDriverHelpEndpoint(self) -> str:
        return "coming soon"

    def getDriverTips(self) -> str:
        return "coming soon"

    def isDriverCommandable(self) -> bool:
        return True

    def handleDriverCommand(self, command: Command) -> ApitaxResponse:
        return super().handleDriverCommand(command) # TODO: Implement a command parser prior to calling super
