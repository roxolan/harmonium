try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Continens exercitia optima',
    'author': 'roxolan',
    'url': 'https://github.com/roxolan/harmonium',
    'download_url': 'https://github.com/roxolan/harmonium/archive/master.zip',
    'author_email': 'roxolanus@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['harmonium'],
    'scripts': [],
    'name': 'harmonium'
}

setup(**config)
