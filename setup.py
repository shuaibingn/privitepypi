from setuptools import setup, find_packages

setup(
    name='privatepypi',
    version="1.0",
    packages=find_packages(),
    include_package_data=False,
    install_requires=["twine"],
    entry_points={
        "console_scripts": [
            "setup = privatepypi.setupfile:main"
        ]
    }
)
