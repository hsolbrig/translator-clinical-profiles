import os
from distutils.core import setup

import clipr

"""
git tag {VERSION}
git push --tags
python setup.py sdist upload -r pypi
"""

VERSION = clipr.__version__

setup(
    name="clipr",
    version=VERSION,
    author="Jordan Matelsky",
    author_email="jordan.matelsky@jhuapl.edu",
    description=("Clinical Profile Generation"),
    license="BSD",
    keywords=[
       "metadata"
    ],
    #url="https://github.com/ ... / ... /tarball/" + VERSION,
    packages=['clipr'],
    scripts=[
       #  'scripts/'
    ],
    classifiers=[],
    install_requires=[
        'pandas',
        'numpy'
    ],
)
