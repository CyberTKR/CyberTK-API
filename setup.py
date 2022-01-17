#!/usr/bin/env python
import os,io
import sys
from setuptools import find_packages, setup

isim = 'CyberTKAPI'
description = 'CyberTK REST API v-1.'
link = 'https://github.com/CyberTKR/CyberTK-API'
mail = 'tolgkr@cybertkr.com'
yazar = 'CyberTK'
tavsiye_py_vers = '>=3.6.0'
version = "v-1"
install_Req = [
      'httpx'
],

import sys

if not (sys.version_info.major == 3 and sys.version_info.minor >= 5):
    print("This script requires Python 3.5 or higher!")
    print("You are using Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)
    
dosyacontrol = os.path.abspath(os.path.dirname(__file__))

try:
    with io.open(os.path.join(dosyacontrol, 'README.md'), encoding='utf-8') as f:
        uzun_acıklama = '\n' + f.read()
except FileNotFoundError:
    uzun_acıklama = description

bilgi = {}
if not version:
    proje_bilgisi = isim.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(dosyacontrol, proje_bilgisi, '__version__.py')) as f:
        exec(f.read(), bilgi)
else:
    bilgi['__version__'] = version

setup(
    name=isim,
    version=bilgi['__version__'],
    description=description,
    long_description=uzun_acıklama,
    long_description_content_type='text/markdown',
    author=yazar,
    author_email=mail,
    python_requires=tavsiye_py_vers,
    url=link,
    packages=find_packages(),
    install_requires=[
        'httpx',
        'httpx[http2]'
    ],
    include_package_data=True,
    license='MIT',
    classifiers=[
      "Programming Language :: Python :: 3.6"
    ]
)
