# Copyright (C) 2020 Samuel Baker

DESCRIPTION = "Create an objected from a shapefile with shapely compatible geometry"
LONG_DESCRIPTION = """
<!--ABOUT THE PROJECT -->
## About The Project
The [Pyshp](https://pypi.org/project/pyshp/1.2.10/) library allows for a pure python approach to reading in Esri 
Shapefile formatted files. This Project uses Pyshp to import these files, but then configures the objects to be 
[Shapely](https://pypi.org/project/Shapely/) style objects. 

This should make it quicker to start new projects involving shapefiles and reduce duplicating code.

All of the source code can be found at the [shapeObject github](https://github.com/sbaker-dev/Shape_object)
"""
LONG_DESCRIPTION_CONTENT_TYPE = "text/markdown"

DISTNAME = 'shapeObject'
MAINTAINER = 'Samuel Baker'
MAINTAINER_EMAIL = 'samuelbaker.researcher@gmail.com'
LICENSE = 'MIT'
DOWNLOAD_URL = "https://github.com/sbaker-dev/ShapeObject"
VERSION = "0.02.0"
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    "pyshp>=2.1.0",
    "Shapely>=1.7.0"
]

PACKAGES = [
    "shapeObject",
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'License :: OSI Approved :: MIT License',
    'Topic :: Scientific/Engineering :: GIS',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

if __name__ == "__main__":

    from setuptools import setup

    import sys

    if sys.version_info[:2] < (3, 7):
        raise RuntimeError("shapeObject requires python >= 3.7.")

    setup(
        name=DISTNAME,
        author=MAINTAINER,
        author_email=MAINTAINER_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type=LONG_DESCRIPTION_CONTENT_TYPE,
        license=LICENSE,
        version=VERSION,
        download_url=DOWNLOAD_URL,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        packages=PACKAGES,
        classifiers=CLASSIFIERS
    )
