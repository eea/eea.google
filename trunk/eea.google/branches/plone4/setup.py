""" EEA Google Installer
"""
import os
from setuptools import setup, find_packages

name = 'eea.google'
path = name.split('.') + ['version.txt']
version = open(os.path.join(*path)).read().strip()

setup(name=name,
      version=version,
      description="Access to Google API.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='EEA google api plone zope python',
      author='Alin Voinea (eaudeweb), European Environment Agency',
      author_email='webadmin@eea.europa.eu',
      url="https://svn.eionet.europa.eu/projects/"
          "Zope/browser/trunk/eea.google",
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      namespace_packages=['eea'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
