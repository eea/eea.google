""" Analytics browser pages
"""
import logging
from zope.component import getUtility
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage
from content import Analytics
from interfaces import IGoogleAnalyticsConnection

logger = logging.getLogger('eea.google')
#
# Abstract browser view
#
class AnalyticsView(BrowserView):
    """ Define common methods
    """
    def _redirect(self, msg):
        if self.request:
            url = self.context.absolute_url()
            IStatusMessage(self.request).addStatusMessage(msg, type='info')
            self.request.response.redirect(url)
        return msg
#
# Add page
#
class AnalyticsAddPage(AnalyticsView):
    """ Add Google Analytics connection
    """
    def __call__(self, **kwargs):
        conn = Analytics()
        if conn.id in self.context.objectIds():
            return self._redirect('Connection exists')
        self.context._setObject(conn.id, conn)
        return self._redirect('Connection added')
#
# Register service
#
class AnalyticsRegisterPage(AnalyticsView):
    """ Register token
    """
    def __call__(self, **kwargs):
        if self.request:
            kwargs.update(self.request.form)

        token = kwargs.get('token', '') or ''

        # Reset tooken
        if not token:
            self.context._token = token
            return self._redirect('Token removed successfully')

        # Update token
        utility = getUtility(IGoogleAnalyticsConnection)
        conn = utility(token)

        # Replace single call token with a session one
        token = conn.token2session()
        if not token:
            return self._redirect(("An error occured during registration process. "
                                   "Please check the log file"))
        self.context._token = token
        return self._redirect('Successfully registered with Google.')

class AnalyticsViewPage(AnalyticsView):
    """ View Google Analytics connection information
    """
    @property
    def status_error(self):
        if not self.context.token:
            return {
                'status': 404,
                'error': 'Not initialized'
            }
        utility = getUtility(IGoogleAnalyticsConnection)
        conn = utility(self.context.token)
        status, error = conn.status
        return {
            'status': status,
            'error': error
        }
