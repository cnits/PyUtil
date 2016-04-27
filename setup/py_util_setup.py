from distutils.core import setup


setup(
    name="CNIT-PyUtil",
    version="0.0.1",
    author="Phong VLam",
    author_email="appstoregugle2310@gmail.com",
    packages=["pyutil"],
    include_package_data=True,
    url="http://github.com/cnits/PyUtil.git",
    description="Implement some of utility library for learning Python",
    install_requires=["pymongo", "pycurl", "lxml"]
)
