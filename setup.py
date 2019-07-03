#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

import os

exec(open('admin_interface/version.py').read())

github_url = 'https://github.com/fabiocaccamo'
package_name = 'django-admin-interface'
package_path = os.path.abspath(os.path.dirname(__file__))
long_description_file_path = os.path.join(package_path, 'README.md')
long_description_content_type = 'text/markdown'
long_description = ''
try:
    with open(long_description_file_path) as f:
        long_description = f.read()
except IOError:
    pass

setup(
    name=package_name,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    include_package_data=True,
    version=__version__,
    description='django-admin-interface is a modern responsive flat admin interface customizable by the admin itself.',
    long_description=long_description,
    long_description_content_type=long_description_content_type,
    author='Fabio Caccamo',
    author_email='fabio.caccamo@gmail.com',
    url='%s/%s' % (github_url, package_name, ),
    download_url='%s/%s/archive/%s.tar.gz' % (github_url, package_name, __version__, ),
    keywords=['django', 'admin', 'interface', 'responsive', 'flat', 'theme', 'custom', 'ui'],
    requires=['django(>=1.7)'],
    install_requires=[
        'django-colorfield >= 0.1, < 1.0',
        'django-flat-theme >= 1.0, < 2.0',
        'django-flat-responsive >= 1.0, < 3.0',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
    ],
    license='MIT',
    test_suite='runtests.runtests'
)
