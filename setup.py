#!/usr/bin/env python

try:
    from setuptools import setup, find_packages, Command
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages, Command


install_requires = [
    'django-taggit'
    'django-markdown',
]

setup(
    name='yaba2',
    version='0.1',
    author='Mark Rogers',
    author_email='xxf4ntxx@gmail.com',
    url='http://github.com/f4nt/yaba2',
    description = 'Simple Blogging Application',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points = {},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)

