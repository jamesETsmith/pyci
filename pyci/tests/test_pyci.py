"""
Unit and regression test for the pyci package.
"""

# Import package, test suite, and other packages as needed
import pyci
import pytest
import sys

def test_pyci_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "pyci" in sys.modules
