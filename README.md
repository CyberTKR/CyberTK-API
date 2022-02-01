## REQUIREDMENT ##
```PY
pip3 install httpx && pip3 install httpx[http2]

Or: python3 setup.py install
```


- Special => LikePost WebAPI: 250:500:1000:3000 
- https://app.cybertkr.com/v-1/LikePost

- Example To Use

```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### APPNAME + USERAGENT #######

_r = _a._appuseragent("chrome") # ANDROID, CHROME
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### APPRANDOM #######

_r = _a._apprandom()
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### WEATHER-API #######

_r = _a._weatherapi('netherlands')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### INSTAGRAM-SEARCH-USER-API #######

_r = _a._instaprofile('_aquariusman')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API
import requests,json
import random
import string

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### SCREEN-SHOTWEB-API #######

_r = _a._screenShotWeb('http://github.com/CyberTKR')
file = open(f"{''.join(random.choices(string.ascii_lowercase, k=10))}.png", "wb")
file.write(_r.content)
file.close()

##########################
```


```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### COVID19-API #######

_r = _a._covid19('tr').json()
_a.GoodPrint(_r)

##########################
```


```PY
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

_a = API(apiKey,version)

####### TIKTOK-SEARCH-USER-API #######

_r = _a._tiktoksearch('username').json()
_a.GoodPrint(_r)

##########################
```

```PY
####### LINEQR #######
from CyberTKAPI.api import API
import requests,json

apiKey = ""
version = "v-1"

a = API(apiKey,version)

_app = "CHROMEOS\t2.5.0\tChrome OS\t1"
_uagnt ="Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36"


_q = a._lineqr(_app,_uagnt)
a.GoodPrint(_q)

_p = a._linepin(_q['Key'],_q['Session'],_app,_uagnt)

if _p["Pincode"]:
  _ur = "\n"
  print(f'{_ur * 1}Pin: {_p["Pincode"]}{_ur * 1}')
  _a = a._lineauthToken(_q['Key'],_q['Session'],_app,_uagnt)
  if _a["authToken"]:
      PrettyPrint = """

      qrCode-API v-1

Pincode: {}
IP: {}
Key: {}
X-Line-Application: {}
QrImage: {}
Session: {}
Certificate: {}
authToken: {}
User-Agent: {}
QR: {}
"""
      print(PrettyPrint.format(_a["Pincode"],_a["IP"],_a["Key"],_a["X-Line-Application"],_a["QrImage"],_a["Session"],_a["Certificate"],_a["authToken"],_a["User-Agent"],_a["QR"]))
else:
    print("Zaman Doldu. !")
```


  

LAST UPDATE: 16/01/2022


LICENSE: Buying me a coffee ☕ or tea 🍵 🥺👈

- 💼 Email, [email](mailto:tolgkr@cybertkr.com) ☕
- 💼 Whatsaap, [link](https://api.whatsapp.com/send?phone=31686208125)☕

<a href="https://www.buymeacoffee.com/cybertkr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

