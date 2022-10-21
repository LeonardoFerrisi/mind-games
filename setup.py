import setuptools
from setuptools import find_packages
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="mindgames",
    version="0.0.1",
    author="Leonardo Ferrisi",
    author_email="ferrisil@union.edu",
    packages=find_packages(),
    description="A package for adding biosensing to your games!",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    python_requires='>=3.8',
    install_requires=["pygame", "brainflow"]
)