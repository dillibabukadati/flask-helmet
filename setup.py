# Created by @dillibk777 at 12/02/23
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flask-helmet',
    version='1.0.0',
    description='A Flask extension for adding security headers to HTTP responses',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'flask',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    author='Dilli Babu Kadati',
    author_email='dillibabukadati777@gmail.com',
    url='https://github.com/dillibk777/flask-helmet',
    keywords='flask security headers helmet'
)
