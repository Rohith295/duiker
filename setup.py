# -*- coding: utf-8 -*-

import sys

import setuptools

if sys.version_info < (3, 5):
    error='Duiker requires Python 3.5 or greater ({version.major}.{version.minor}.{version.micro} installed).'.format(version=sys.version_info)
    print(error, file=sys.stderr)
    sys.exit(1)


tests_require = [
    'mock',
    'pytest',
    'pytest-cov',
    'pytest-helpers-namespace',
]


setuptools.setup(
    name='duiker',
    version='0.1.0',
    url='https://github.com/benwebber/duiker/',

    description='Automatically index your shell history in a full-text search database. Magic!',
    long_description=open('README.rst').read(),

    author='Ben Webber',
    author_email='benjamin.webber@gmail.com',

    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},

    install_requires=['click==6.6'],
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    extras = {
        'test': tests_require,
    },

    zip_safe=False,

    entry_points={
        'console_scripts': [
            'duiker = duiker.cli:cli',
        ],
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
