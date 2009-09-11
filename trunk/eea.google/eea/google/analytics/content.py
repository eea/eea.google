from zope.interface import implements
from interfaces import IAnalytics
from OFS.Folder import Folder

class Analytics(Folder):
    """ Google Analytics connection
    """
    implements(IAnalytics)
    id = 'analytics'
    title = 'Google Analytics'
    meta_type = 'Google Analytics'
    portal_type = 'Google Analytics'
    _token = ''

    @property
    def token(self):
        return self._token
