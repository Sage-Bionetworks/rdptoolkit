import os
import setuptools


def read(rel_path: str) -> str:
    """Read file"""
    # type: (str) -> str
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(os.path.join(here, rel_path)) as fp:
        return fp.read()


def get_version(rel_path: str) -> str:
    """Get version from __init__.py: following pip setup.py example
    https://github.com/pypa/pip/blob/master/setup.py#L11
    """
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            # __version__ = "0.9"
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    raise RuntimeError("Unable to find version string.")


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    # basic
    name='rdptoolkit',
    version=get_version("rdptoolkit/__init__.py"),

    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': ['rdptoolkit=rdptoolkit.cli.__main__:main']
    },

    # requirements
    python_requires='>=3.9.*',
    install_requires=[
        'click==8.0.3',
        'elasticsearch==7.15.2',
        'elasticsearch-dsl==7.4.0'
    ],

    # metadata to display on PyPI
    description='RDP Toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://nlpsandbox.io',
    author='Thomas Schaffter',
    author_email='thomas.schaffter@sagebionetworks.org',
    license='Apache',
    project_urls={
        "Source Code": "https://github.com/Sage-Bionetworks/resource-discovery-portal-tools",
        "Bug Tracker": "https://github.com/Sage-Bionetworks/resource-discovery-portal-tools/issues",
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ]
)
