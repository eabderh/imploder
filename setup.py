
from setuptools import setup, find_packages

def fromfile(path):
    with open(path) as f:
        return f.read()

setup(
    # basic
    name='imploder',
    version='0.1.0',
    description='reload modules',
    long_description=fromfile('README.md'),
    # author
    author='Elias Abderhalden',
    author_email='elias@bytekite.io',
    # dist
    license=fromfile('LICENSE.txt'),
    #url=''
    # module
    packages=find_packages(exclude=('tests', 'docs'))
)

