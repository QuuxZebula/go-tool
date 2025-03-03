#!/usr/bin/env python
# Copyright (c) 2002-2008 ActiveState Software
# Author: Trent Mick (trentm@gmail.com)
"""Quick directory changing (super-cd)

'go' is a simple command line script to simplify jumping between
directories in the shell. You can create shortcut names for commonly
used directories and invoke 'go <shortcut>' to switch to that directory
-- among other little features.
"""

from setuptools import setup
import os
import sys

# Add the 'lib' directory to the Python path temporarily
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from go import __version__
sys.path.pop(0)  # removing temp path.


# Function to read the content of a file
def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname),
              encoding="utf-8") as f:
        return f.read()


# Classifiers for the project
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Shells",
    "Topic :: Utilities",
]

# Define the setup configuration
setup(
    name="go-tool",  # Updated the name
    version=__version__,
    author="Trent Mick",
    author_email="trentm@gmail.com",
    url="http://code.google.com/p/go-tool/",  # Keep the original URL
    license="MIT",  # Use the short identifier
    platforms=["any"],
    description="Quick directory changing (super-cd)",
    long_description=read("README.md"),  # Read long description from README.md
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    package_dir={"": "lib"},  # Specify the location of the packages
    packages=[""],  # Add an empty package so we can add go.py with py_modules
    py_modules=["go"],  # Add go as a py_module
    python_requires=">=3.7",
    install_requires=[
        "pywin32; platform_system=='Windows'",  # windows specific dependency
    ],
    extras_require={
        "dev": [
            "pytest",
            "flake8",
            "black",
            "mypy",
        ],
    },
)
