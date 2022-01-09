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

api = API(apiKey,version)

####### APPNAME + USERAGENT #######

res = api._appuseragent("chrome") # ANDROID, CHROME
print(json.dumps(res, indent=4))

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### APPRANDOM #######

res = api._apprandom()
print(json.dumps(res, indent=4))

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### WEATHER-API #######

res = api._weatherapi('netherlands')
print(json.dumps(res, indent=4))

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### INSTAGRAM-SEARCH-USER-API #######

res = api._instaprofile('_aquariusman')
print(json.dumps(res, indent=4))

##########################
```

```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### SCREEN-SHOTWEB-API #######

res = api._screenShotWeb('http://github.com/CyberTKR')
file = open(f"{''.join(random.choices(string.ascii_lowercase, k=10))}.png", "wb")
file.write(res.content)
file.close()

##########################
```


```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### COVID19-API #######

res = api._covid19('tr').json()
print(json.dumps(res, indent=4))

##########################
```


```PY
from CyberTKAPI import API
import requests,json

apiKey = ""
version = "v1-beta"

api = API(apiKey,version)

####### TIKTOK-SEARCH-USER-API #######

res = api._tiktoksearch('username').json()
print(json.dumps(res, indent=4))

##########################
```
LAST UPDATE: 09/01/2022


LICENSE: Buying me a coffee ☕ or tea 🍵 🥺👈

- 💼 Email, [email](mailto:tolgkr@cybertkr.com) ☕
- 💼 Whatsaap, [link](https://api.whatsapp.com/send?phone=31686208125)☕

<a href="https://www.buymeacoffee.com/cybertkr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

