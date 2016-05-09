try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ipodcopier',
    version='0.0.1',
    description='Music file copier from iPod format',
    long_description=readme,
    author='Kristjan Olafur Olafsson',
    author_email='kristjanola13@ru.is',
    license=license,
    packages=['ipodcopier']
)
