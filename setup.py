# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages


setup(
    name='docs2confluence',
    version='0.1.0',
    description='Solution for uploading markdown formatted documents to Atlassian Confluence',
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ),
    author='Nikita Grishko',
    author_email='grin.minsk+github@gmail.com',
    url='https://github.com/Gr1N/docs2confluence',
    license='MIT',
    packages=find_packages(),
    install_requires=(
        'setuptools',
        'requests==2.5.1',
        'sh==1.11',
    ),
    extras_require={
        'development': (
            'flake8',
            'check-manifest',
        ),
    },
    include_package_data=True,
    zip_safe=False,
    scripts=(
        'docs2confluence',
    )
)
