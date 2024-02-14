"""A setuptools based setup module."""

from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    # This is the name of your project. The first time you publish this
    # package, this name will be registered for you. It will determine how
    # users can install this project, e.g.:
    #
    # $ pip install sampleproject
    #
    # And where it will live on PyPI: https://pypi.org/project/sampleproject/
    #
    name="bireysel_algo",  # Required
    version="2.1.0",  # Required
    
    description="TEST ON Bireysel METHOD FOR CLASSIFICATION PROBLEMS",  # Optional
    long_description=long_description,  # Optional

    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/dahmansphi/bireysel_algo_v1.git",  # Optional
    
    author="Dr. Deniz Dahman's",  # Optional
    author_email="dahmansphi@gmail.com",  # Optional
    License = "GPL-3.0",
    Requires = "None",
    # Classifiers help users find your project by categorizing it.
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    
    keywords="classification, bireysel, machine learning",  # Optional
    
    package_dir={"": "src"},  # Optional
    #
    packages=find_packages(where="src"),  # Required
    
    python_requires=">=3.9",
    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    # install_requires=["peppercorn"],  # Optional

)