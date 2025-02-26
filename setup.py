from setuptools import find_packages, setup

setup(
    name="typecast-sdk",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
) 