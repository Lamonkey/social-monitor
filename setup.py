from setuptools import find_packages
from setuptools import setup

setup(
    name='sherlockModule',
    version='0.1.0',
    packages=find_packages('src/sherlock'),
    package_dir={'': 'src/sherlock'},
)