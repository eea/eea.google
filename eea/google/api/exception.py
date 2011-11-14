""" exception module """

class GoogleClientError(Exception):
    """ General Google error (error accessing Google API)
    """
    def __init__(self, reason):
        super(GoogleClientError, self).__init__(reason)
        self.reason = reason

    def __repr__(self):
        return 'GoogleError: %s' % self.reason

    def __str__(self):
        return 'GoogleError: %s' % self.reason
