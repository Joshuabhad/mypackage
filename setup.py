from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Joshuabhad/mypackage',
    author='Joshua Bhadrachellam',
    author_email='joshuabhad@gmail.com'
)
