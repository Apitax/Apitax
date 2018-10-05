from apitaxcore.catalog.Catalog import Catalog


class EndpointCatalog(Catalog):

    def __init__(self):
        super().__init__("endpoints")

    def add(self, name, label, value, summary='', help='', driver='', examples=[]):
        item = {name: {'label': label, 'value': value, 'summary': summary, 'help': help, 'driver': driver,
                       'examples': examples}}
        super().add(item)
