"""
molssi_devops
Some math functions in a package
"""

# Add imports here
from .molssi_math import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
