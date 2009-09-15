import datetime
from zope.interface import implements
from OFS.Folder import Folder

from interfaces import IAnalytics
from interfaces import IAnalyticsReport

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

class AnalyticsReport(Folder):
    """ Google Analytics report
    """
    implements(IAnalyticsReport)

    meta_type = "Google Analytics Report"
    portal_type = "Google Analytics Report"
    title = ''

    table = ''
    dimensions = ()
    metrics = ()
    filters = ''
    sort = ''
    start_date = datetime.date(2009, 1, 1)
    end_date = datetime.date(2019, 12, 31)
    start_index = 1
    max_results = 5
