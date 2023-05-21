import setuptools

from pyfilter import __version__, __author__, __program__


setuptools.setup(
      name=__program__,
      version=__version__,
      description='A simple web server for serving files and directories.',
      author=__author__,
      packages=setuptools.find_packages(),
      package_data={'pyfilter': ['templates/*.html']},
      include_package_data=True,
      install_requires=['flask']
      )
