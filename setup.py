import os, io
import sys
from setuptools import find_packages, setup

isim = "CyberTKAPI"
description = "CyberTK REST API v2"
link = "https://github.com/CyberTKR/CyberTK-API"
mail = "tolg@cybertkr.com"
yazar = "CyberTK"
tavsiye_py_vers = ">=3.6.0"
version = "2.8"
install_Req = ["httpx", "httpx[http2]"]
if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    print("This script requires Python 3.6 or higher!")
    print(
        "You are using Python {}.{}.".format(
            sys.version_info.major, sys.version_info.minor
        )
    )
    sys.exit(1)
dosyacontrol = os.path.abspath(os.path.dirname(__file__))
try:
   with io.open(os.path.join(dosyacontrol,'README.md'),encoding='utf-8') as f:
        uzun_acıklama='\n'+f.read()
except FileNotFoundError:
    uzun_acıklama=description
    
bilgi = {}
if not version:
    proje_bilgisi = isim.lower().replace("-", "_").replace(" ", "_")
    with open(os.path.join(dosyacontrol, proje_bilgisi, "__version__.py")) as f:
        exec(f.read(), bilgi)
else:
    bilgi["__version__"] = version
setup(
    name=isim,
    version=bilgi["__version__"],
    description=description,
    long_description=uzun_acıklama,
    long_description_content_type="text/markdown",
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
