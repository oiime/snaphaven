#!/usr/bin/env python
from setuptools import setup

setup(
    name="snaphaven",
    version="0.0.1",
    description="moves cassandra snapshots to a different local directory as they are written",
    url="https://github.com/qdatum/snaplocal",
    download_url='https://github.com/qdatum/qdatum-python-driver/tarball/0.0.1',
    author="Itamar Maltz",
    author_email="ism@qdatum.io",
    install_requires=['pyinotify', 'argparse'],
    platforms=["any"],
    license='MIT',
    keywords="cassandra",
    scripts=['snaphaven'],
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
    ],
)
