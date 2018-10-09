from setuptools import setup, find_packages

NAME = "import_package"
VERSION = "1.0.0"

REQUIRES = [
    'configargparse',
    'bravado',
    'apscheduler']
setup(
    name=NAME,
    version=VERSION,
    description="test import github package",
    url="",
    install_requires=REQUIRES,
    packages=find_packages()
)
