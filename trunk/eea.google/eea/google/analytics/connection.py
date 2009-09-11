from eea.google.api.connection import Connection
from interfaces import IGoogleAnalyticsConnection

class GoogleAnalyticsConnection(object):
    """ Access Google Analytics
    """
    def __call__(self, token):
        self.connection = Connection(token)
        return self.connection
