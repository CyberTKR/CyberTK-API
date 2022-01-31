## REQUIREDMENT ##
```PY
pip3 install httpx && pip3 install httpx[http2]

Or: python3 setup.py install
```


- Special => LikePost WebAPI: 250:500:1000:3000 
- https://app.cybertkr.com/v-1/LikePost

- Example To Use

```PY
from CyberTKAPI import API
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
from CyberTKAPI import API
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
from CyberTKAPI import API
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
from CyberTKAPI import API
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
from CyberTKAPI import API
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
from CyberTKAPI import API
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
from CyberTKAPI import API
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

import requests
import json,time,pyqrcode
_H = {
  "ApiKey": "",
  'API-Version': "v-1",
  "AppName": "CHROMEOS\t2.5.0\tChrome OS\t1",
  "UserAgent": "Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36"
}
url='https://app.cybertkr.com/v-1/qrCode'
_d=json.loads(requests.session().post(url,headers=_H).text)
print(json.dumps(_d,indent=4))
_t=time.time()
while True:
	_p='https://app.cybertkr.com/v-1/GetResult/{}'.format(_d['Key']);_pd=json.loads(requests.session().post(_p).text);print('Giris yapilmasi bekleniyor.!');time.sleep(5)
	if time.time()-_t<int(30):
		if _pd['Pincode']!='':print('**********************\n\nPincode: {}\n\n**********************'.format(_pd['Pincode']));time.sleep(10);_pd=json.loads(requests.session().post(_p).text);print(json.dumps(_pd,indent=4));break
	else:pass;break

##########################
```


  

LAST UPDATE: 16/01/2022


LICENSE: Buying me a coffee ☕ or tea 🍵 🥺👈

- 💼 Email, [email](mailto:tolgkr@cybertkr.com) ☕
- 💼 Whatsaap, [link](https://api.whatsapp.com/send?phone=31686208125)☕

<a href="https://www.buymeacoffee.com/cybertkr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

