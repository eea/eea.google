""" Google API
"""
import urllib2
import logging
from exception import GoogleClientError
logger = logging.getLogger('eea.google.api')

class Connection(object):
    """ Google connection
    """
    def __init__(self, token):
        self.token = token
        self.domain = 'https://www.google.com'

    @property
    def headers(self):
        """ Request headers
        """
        return {
            'User-Agent': 'eea.google.api',
            'Authorization': 'AuthSub token="%s"' % self.token,
        }

    @property
    def status(self):
        """ Validate token
        """
        scope = '/accounts/AuthSubTokenInfo'
        try:
            response = self(scope)
        except GoogleClientError, err:
            return (403, err)
        return response.code, response.msg

    def token2session(self):
        """ Replace single call token with a session one.
        """
        scope = '/accounts/AuthSubSessionToken'
        try:
            response = self(scope)
        except GoogleClientError, err:
            logger.exception(err)
            return None

        data = response.readlines()
        token = [item.strip() for item in data
                 if item.lower().strip().startswith('token')]

        if not token:
            logger.exception('\n'.join(data))
            return None
        token = token[0].split('=')
        if not len(token) > 1:
            logger.exception('\n'.join(data))
            return None

        self.token = token[1]
        return self.token

    def __call__(self, scope):
        """ Connection to google API
        """
        request = urllib2.Request(self.domain + scope, headers=self.headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, err:
            logger.exception(err)
            raise GoogleClientError(err)
        return response
