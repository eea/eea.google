from xml.dom import minidom
from zope.app.schema.vocabulary import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.component import getUtility
from interfaces import IGoogleAnalyticsConnection

class TablesVocabulary(object):
    """ Widget position in page
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        utility = getUtility(IGoogleAnalyticsConnection)
        conn = utility(context.token)
        scope = '/analytics/feeds/accounts/default'
        response = conn.connect(scope)
        if not response:
            return SimpleVocabulary(())

        tables = []
        xml = response.read()
        dom = minidom.parseString(xml)
        accounts = dom.getElementsByTagName('entry')
        for account in accounts:
            for prop in account.childNodes:
                if prop.nodeName != 'dxp:tableId':
                    continue
                key = prop.childNodes[0].data
                tables.append(SimpleTerm(key, key, key.replace('ga:', '')))
        return SimpleVocabulary(tables)
Tables = TablesVocabulary()

class DimensionsVocabulary(object):
    """ Google analytics report dimensions
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        dimensions = [
            'ga:browser',
            'ga:browserVersion',
            'ga:city',
            'ga:connectionSpeed',
            'ga:continent',
            'ga:countOfVisits',
            'ga:country',
            'ga:date',
            'ga:day',
            'ga:daysSinceLastVisit',
            'ga:flashVersion',
            'ga:hostname',
            'ga:hour',
            'ga:javaEnabled',
            'ga:language',
            'ga:latitude',
            'ga:longitude',
            'ga:month',
            'ga:networkDomain',
            'ga:networkLocation',
            'ga:pageDepth',
            'ga:operatingSystem',
            'ga:operatingSystemVersion',
            'ga:region',
            'ga:screenColors',
            'ga:screenResolution',
            'ga:subContinent',
            'ga:userDefinedValue',
            'ga:visitorType',
            'ga:week',
            'ga:year',
            'ga:adContent',
            'ga:adGroup',
            'ga:adSlot',
            'ga:adSlotPosition',
            'ga:campaign',
            'ga:keyword',
            'ga:medium',
            'ga:referralPath',
            'ga:source',
            'ga:exitPagePath',
            'ga:landingPagePath',
            'ga:pagePath',
            'ga:pageTitle',
            'ga:affiliation',
            'ga:daysToTransaction',
            'ga:productCategory',
            'ga:productName',
            'ga:productSku',
            'ga:transactionId',
            'ga:searchCategory',
            'ga:searchDestinationPage',
            'ga:searchKeyword',
            'ga:searchKeywordRefinement',
            'ga:searchStartPage',
            'ga:searchUsed',
        ]
        dimensions.sort()
        return SimpleVocabulary([SimpleTerm(x, x, x.replace('ga:', ''))
                                 for x in dimensions])

Dimensions = DimensionsVocabulary()

class MetricsVocabulary(object):
    """ Google analytics report metrics
    """
    implements(IVocabularyFactory)

    def __call__(self, context=None):
        metrics = [
            'ga:bounces',
            'ga:entrances',
            'ga:exits',
            'ga:newVisits',
            'ga:pageviews',
            'ga:timeOnPage',
            'ga:timeOnSite',
            'ga:visitors',
            'ga:visits',
            'ga:adClicks',
            'ga:adCost',
            'ga:CPC',
            'ga:CPM',
            'ga:CTR',
            'ga:impressions',
            'ga:uniquePageviews',
            'ga:itemRevenue',
            'ga:itemQuantity',
            'ga:transactionRevenue',
            'ga:transactions',
            'ga:transactionShipping',
            'ga:transactionTax',
            'ga:uniquePurchases',
            'ga:searchDepth',
            'ga:searchDuration',
            'ga:searchExits',
            'ga:searchRefinements',
            'ga:searchUniques',
            'ga:searchVisits',
            'ga:goal1Completions',
            'ga:goal2Completions',
            'ga:goal3Completions',
            'ga:goal4Completions',
            'ga:goalCompletionsAll',
            'ga:goal1Starts',
            'ga:goal2Starts',
            'ga:goal3Starts',
            'ga:goal4Starts',
            'ga:goalStartsAll',
            'ga:goal1Value',
            'ga:goal2Value',
            'ga:goal3Value',
            'ga:goal4Value',
            'ga:goalValueAll',
        ]
        metrics.sort()
        return SimpleVocabulary([SimpleTerm(x, x, x.replace('ga:', ''))
                                 for x in metrics])
Metrics = MetricsVocabulary()
