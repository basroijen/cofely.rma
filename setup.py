# -*- coding: utf-8 -*-
"""
This module contains the tool of cofely.rma
"""
import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

long_description = (
    read('README.txt')
    + '\n' +
    'Change history\n'
    '**************\n'
    + '\n' +
    read('CHANGES.txt')
    + '\n' +
    'Detailed Documentation\n'
    '**********************\n'
    + '\n' +
    read('cofely', 'rma', 'README.txt')
    + '\n' +
    'Contributors\n'
    '************\n'
    + '\n' +
    read('CONTRIBUTORS.txt')
    + '\n' +
    'Download\n'
    '********\n')

#tests_require = ['zope.testing']

setup(name='cofely.rma',
      version=version,
      description="Handle RMA's in Plone",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='Plone Cofely RMA',
      author='Bas Roijen',
      author_email='bas.roijen@cofely-gdfsuez.nl',
      url='http://cofely-experts.info',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cofely', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'Products.Archetypes',
                        'plone.app.portlets',
                        # -*- Extra requirements: -*-
                        'Products.DataGridField',
                        ],
#      tests_require=tests_require,
#      extras_require=dict(tests=tests_require),
#      test_suite='cofely.rma.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
#      setup_requires=["PasteScript"],
#      paster_plugins=["ZopeSkel"],
      )
