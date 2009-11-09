try:
    import zope.annotation
except ImportError:
    #BBB Plone 2.5
    from os.path import dirname
    from Globals import package_home
    from Products.CMFCore import utils as cmfutils
    from Products.CMFCore.DirectoryView import registerDirectory

    ppath = cmfutils.ProductsPath
    cmfutils.ProductsPath.append(dirname(package_home(globals())))
    registerDirectory('skins', globals())
    cmfutils.ProductsPath = ppath
