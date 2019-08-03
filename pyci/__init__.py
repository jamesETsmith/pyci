"""
PyCI
A C++ library and Python wrapper for CI and approximate CI methods.
"""

# Add imports here
from .pyci import *

# Pybind11 Wrapped C++
from .lib import example

# Handle versioneer
from ._version import get_versions

versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
