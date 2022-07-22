from setuptools import setup, find_packages

setup(
    name='validator',
    version="0.0.001",
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='validator'),
    package_dir={"": "validator"},
)
