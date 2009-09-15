import datetime
from zope.interface import Interface
from zope import schema

class IAnalytics(Interface):
    """ Google Analytics connection
    """
    token = schema.TextLine(title=u"Authentication token")

class IAnalyticsReport(Interface):
    """ Google Analytics report
    """
    title = schema.TextLine(
        title=u"Title",
        description=u"Report title",
        required=True,
    )

    table = schema.Choice(
        title=u"Table id",
        description=u"The table id of the profile to request data from. Table id's you can access are listed in the account feed.",
        required=True,
        vocabulary="eea.google.analytics.tables"
    )

    metrics = schema.Choice(
        title=u'Metrics',
        description=u"The metrics data to be retrieved from the API. A single request is limited to a maximum of 10 metrics.",
        vocabulary="eea.google.analytics.metrics",
        required=True
    )

    dimensions = schema.Choice(
        title=u"Dimensions",
        description=u"The dimension data to be retrieved from the API. A single request is limited to a maximum of 7 dimensions.",
        vocabulary="eea.google.analytics.dimensions",
        required=True,
    )

    start_date = schema.Date(
        title=u"Start date",
        description=u"Beginning date to retrieve data.",
        required=True,
        default=datetime.date(2009, 1, 1)
    )

    end_date = schema.Date(
        title=u"End date",
        description=u"Final date to retrieve data.",
        required=True,
        default=datetime.date(2019, 12, 31)
    )

    filters = schema.TextLine(
        title=u"Filters",
        description=u"Specifies a subset of all data matched in analytics. This tool automatically URI encodes the parameter.",
        required=False,
        default=u''
    )

    sort = schema.TextLine(
        title=u"Sort",
        description=u"The order and direction to retrieve the results. Can have multiple dimensions and metrics.",
        required=False,
        default=u''
    )

    start_index = schema.Int(
        title=u"Start index",
        description=u"Use this parameter to request more rows from the API. For example if your query matches 100,000 rows, the API will only return a subset of them and you can use this parameter to request different subsets. The index starts from 1 and the default is 1.",
        required=False,
        default=1
    )

    max_results = schema.Int(
        title=u"Max results",
        description=u"Maximum number of results to retrieve from the API. The default is 1,000 but can be set up to 10,000.",
        required=False,
        default=5
    )

class IGoogleAnalyticsConnection(Interface):
    """ Access google API within analytics scope
    """
