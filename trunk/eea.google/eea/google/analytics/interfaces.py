from zope.interface import Interface
from zope.schema import TextLine

class IAnalytics(Interface):
    """ Google Analytics connection
    """
    token = TextLine(title=u"Authentication token")

class IGoogleAnalyticsConnection(Interface):
    """ Access google API within analytics scope
    """
