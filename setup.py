from setuptools import setup, find_packages

setup(
    name='my_validator',
    version="0.0.001",
    extras_require=dict(tests=['pytest']),
    packages=find_packages(where='my_validator'),
    package_dir={"": "my_validator"},
)
