from setuptools import setup
""" work in progress, this will be reviewed """
setup(name='clearsky',
      version='0.9',
      description='ClouDNS API client and library',
      url='http://github.com/jmporcelg/',
      include_package_data=True,
      author='Jose Porcel',
      author_email='jose@jporcel.net',
      license='GPL2',
      install_requires=[
        'docopt',
        'pprint',
        'configparser',
        'requests',
    ],
      zip_safe=True)
