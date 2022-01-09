## REQUIREDMENT ##
```PY
pip3 install httpx && pip3 install httpx[http2]

Or: python3 setup.py install
```

- Example To Use

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### APPNAME + USERAGENT #######

_r = api._appuseragent("chrome") # ANDROID, CHROME
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### APPRANDOM #######

_r = _a._apprandom()
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### WEATHER-API #######

_r = _a._weatherapi('netherlands')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### INSTAGRAM-SEARCH-USER-API #######

_r = _a._instaprofile('_aquariusman')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI import API
import requests,json
import random
import string

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### SCREEN-SHOTWEB-API #######

_r = _a._screenShotWeb('http://github.com/CyberTKR')
file = open(f"{''.join(random.choices(string.ascii_lowercase, k=10))}.png", "wb")
file.write(_r.content)
file.close()

##########################
```


```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### COVID19-API #######

_r = _a._covid19('tr').json()
_a.GoodPrint(_r)

##########################
```


```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

_a = API(apiKey,version)

####### TIKTOK-SEARCH-USER-API #######

_r = api._tiktoksearch('username').json()
_a.GoodPrint(_r)

##########################
```
LAST UPDATE: 09/01/2022


LICENSE: Buying me a coffee ☕ or tea 🍵 🥺👈

- 💼 Email, [email](mailto:tolgkr@cybertkr.com) ☕
- 💼 Whatsaap, [link](https://api.whatsapp.com/send?phone=31686208125)☕

<a href="https://www.buymeacoffee.com/cybertkr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

