# -*- coding: utf-8 -*-
import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-kongclient',
    version='1.1.0',
    author='HaiNT',
    author_email='tronghaibk2008@gmail.com',
    description='A python library for the Kong admin API',
    long_description=long_description,
    url='https://github.com/haintd/python-kongclient',
    packages=setuptools.find_packages(),
    package_dir={'kong_client': ''},
    install_requires=['requests'],
    include_package_data=True,
    license='BSD',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    python_requires='>=3.6'
)
