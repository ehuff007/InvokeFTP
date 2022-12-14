# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="invokeftp",
    version="0.0.1",
    description="Small library to perform FTP uploading/downloading similarly to PS' Invoke-WebRequest",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehuff007/InvokeFTP/",
    author="ehuff007",
    author_email="ehuff007@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=["invokeftp"],
    include_package_data=True,
    install_requires=["ipaddress"]
)