try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': "CNIT-PyUtil",
    'description': "Implement some of utility library for learning Python",
    'url': "http://github.com/cnits/PyUtil.git",
    'author': "Phong VLam",
    'author_email': "appstoregugle2310@gmail.com",
    'packages': ["pyutil"],
    'include_package_data': True,
    'install_requires': ["pymongo", "pycurl", "lxml"],
    'scripts': [],
    'version': "0.0.1"
}
setup(**config)
