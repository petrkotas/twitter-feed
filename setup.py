#!/usr/bin/env python
from setuptools import setup, find_packages


__version__ = 1.0


def read(fname):
    with open(fname) as fd:
        content = fd.read()
    return content


setup(
    name='Twitter feed',
    version=__version__,
    description='Converts twitter feed to atom',
    long_description=read('README.md'),
    url='https://github.com/petrkotas/twitter-feed',
    packages=find_packages(exclude=('tests',)),
    setup_requires=['pytest-runner'],
    install_requires=[
        'click>=6.7',
        'feedparser>=5.2.1',
        'Flask>=0.12',
        'Flask-Script>=2.0.5',
        'gevent>=1.2.1',
        'greenlet>=0.4.12',
        'itsdangerous>=0.24',
        'Jinja2>=2.9.5',
        'lazy-object-proxy>=1.2.2',
        'MarkupSafe>=1.0',
        'oauthlib==2.0.1',
        'py>=1.4.32',
        'python-dateutil>=2.6.0',
        'requests>=2.13.0',
        'requests-oauthlib>=0.8.0'
        'six>=1.10.0',
        'Werkzeug>=0.12',
    ],
    entry_points={
        'console_scripts': [
            'twitter-feed=twitter_feed.server:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='MIT License'
)
