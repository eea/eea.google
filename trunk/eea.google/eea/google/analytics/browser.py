""" Analytics browser pages
"""
import logging

from zope.component import getUtility
from zope.formlib.form import Fields, applyChanges
from plone.app.form.base import EditForm, AddForm
from zope.app.container.interfaces import INameChooser

from Acquisition import aq_inner, aq_parent
from Products.Five import BrowserView
from Products.statusmessages.interfaces import IStatusMessage

from content import Analytics, AnalyticsReport
from interfaces import IGoogleAnalyticsConnection, IAnalyticsReport

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

    def remove(self, **kwargs):
        """ Remove connection
        """
        if self.request:
            kwargs.update(self.request.form)

        doc_id = kwargs.get('id', '')
        if not doc_id or doc_id not in self.context.objectIds():
            return self._redirect('Invalid id: %s' % doc_id)

        self.context.manage_delObjects(ids=[doc_id,])
        self._redirect('Object deleted')
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
#
# Analytics report views
#
class ReportAddPage(AddForm):
    """ Add page
    """
    form_fields = Fields(IAnalyticsReport)

    def create(self, data):
        name = INameChooser(self.context).chooseName(data.get('title', ''), None)
        ob = AnalyticsReport(id=name)
        applyChanges(ob, self.form_fields, data)
        return ob

    def add(self, obj):
        name = obj.getId()
        self.context[name] = obj
        self._finished_add = True
        return obj

    def nextURL(self):
        return "."

class ReportEditPage(EditForm):
    """ Edit page
    """
    form_fields = Fields(IAnalyticsReport)

class ReportViewPage(BrowserView):
    """ Index xml
    """
    def __init__(self, context, request):
        super(BrowserView, self).__init__(context, request)
        self.token = aq_parent(aq_inner(self.context)).token

    def error_xml(self, query):
        res = ['<?xml version="1.0" ?>']
        res.append('<error>')
        res.append('<query><![CDATA[%s]]></query>' % query)
        res.append('</error>')
        return '\n'.join(res)

    def __call__(self, **kwargs):
        scope = '/analytics/feeds/data'
        query = {
            'ids': self.context.table,
            'dimensions': self.context.dimensions,
            'metrics': self.context.metrics,
            'filters': self.context.filters,
            'sort': self.context.sort,
            'start-date': str(self.context.start_date),
            'end-date': str(self.context.end_date),
            'start-index': self.context.start_index,
            'max-results': self.context.max_results,
        }
        # Filter None parameters
        query = dict((key, value) for key, value in query.items() if value)

        utility = getUtility(IGoogleAnalyticsConnection)
        conn = utility(self.token)
        response = conn.connect(scope=scope, data=query, method='GET')

        self.request.response.setHeader('content-type', 'text/xml')
        if not response:
            return self.error_xml(query)
        return response.read()
