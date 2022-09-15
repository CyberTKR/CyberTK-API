import os, io
import sys
from setuptools import find_packages, setup, Extension

isim = "CyberTKAPI"
description = "CyberTK REST API v2"
link = "https://github.com/CyberTKR/CyberTK-API"
mail = "tolg@cybertkr.com"
yazar = "CyberTK"
tavsiye_py_vers = ">=3.6.0"
version = "2.9.2"
install_Req = ["httpx==0.19.0", "httpx[http2]"]
if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    print("This script requires Python 3.6 or higher!")
    print(
        "You are using Python {}.{}.".format(
            sys.version_info.major, sys.version_info.minor
        )
    )
    sys.exit(1)

setup(
    name=isim,
    version=version,
    description=description,
    long_description="README.md",
    long_description_content_type='text/markdown',
    author=yazar,
    author_email=mail,
    python_requires=tavsiye_py_vers,
    url=link,
    packages=find_packages(),
    install_requires=install_Req,
    include_package_data=True,
    license="MIT",
    classifiers=["Programming Language :: Python :: 3.6"],
)
