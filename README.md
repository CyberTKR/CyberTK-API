## REQUIREDMENT ##
```PY
$ pip3 install httpx && pip3 install httpx[http2]

$ pip3 install CyberTKAPI

$ pip3 install --upgrade CyberTKAPI

```


- Special => LikePost WebAPI: 250:500:1000:3000 
- https://api.cybertkr.com/v2/LikePost

- Example To Use

> To access the API, only use the url paths given to you.
If you enter a different url path or endpoint, your ip address will be banned indefinitely.





```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### APPNAME + USERAGENT #######

_r = _a._appuseragent("desktopmac") # ANDROID, CHROME, DESKTOPMAC, DESKTOPWIN
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### APPRANDOM #######

_r = _a._apprandom()
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### WEATHER-API #######

_r = _a._weatherapi('netherlands')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### INSTAGRAM-SEARCH-USER-API #######

_r = _a._instaprofile('_aquariusman')
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API
import random
import string

apiKey = "LosAngeles"
version = "v2"

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

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### COVID19-API #######

_r = _a._covid19('tr').json()
_a.GoodPrint(_r)

##########################
```


```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

_a = API(apiKey,version)

####### TIKTOK-SEARCH-USER-API #######

_r = _a._tiktoksearch('username').json()
_a.GoodPrint(_r)

##########################
```

```PY
from CyberTKAPI.api import API

apiKey = "LosAngeles"
version = "v2"

a = API(apiKey,version)

####### LINEQR #######

_app = "CHROMEOS\t2.5.0\tChrome OS\t1"
_uagnt ="Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36"


qrResult = a._lineqr(_app,_uagnt)
a.GoodPrint(qrResult)

pinResult = a._linepin(qrResult['Key'],qrResult['Session'],_app,_uagnt)

if pinResult["Pincode"]:
  _ur = "\n"
  print(f'{_ur * 1}Pin: {pinResult["Pincode"]}{_ur * 1}')
  authResult = a._lineauthToken(qrResult['Key'],qrResult['Session'],_app,_uagnt)
  if authResult["authToken"]:
      PrettyPrint = """

      qrCode-API v2

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
      print(PrettyPrint.format(authResult["Pincode"],authResult["IP"],authResult["Key"],authResult["X-Line-Application"],authResult["QrImage"],authResult["Session"],authResult["Certificate"],authResult["authToken"],authResult["User-Agent"],authResult["QR"]))
else:
    print("Zaman Doldu. !")
    
##########################


####### LINEQR-IMAGE SELFBOT #######

from CyberTKAPI.api import API

_app = "CHROMEOS\t2.5.0\tChrome OS\t1"
_uagnt ="Mozilla/5.0 (X11; CrOS x86_64 14268.67.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.111 Safari/537.36"

apiKey = "LosAngeles"
version = "v2"

a = API(apiKey,version)
qrResult = a._lineqr(_app,_uagnt)
print(f'QRCode Image: {qrResult["QrImage"]}')
print(f'QR: {qrResult["QR"]}')
pinResult = a._linepin(qrResult['Key'],qrResult['Session'],_app,_uagnt)
print(f'Pincode: {pinResult["Pincode"]}')
authResult = a._lineauthToken(qrResult['Key'],qrResult['Session'],_app,_uagnt)
authToken,certificate = authResult["authToken"],authResult["Certificate"]
print(f'authToken: {authToken}')
print(f'Certificate: {certificate}')
    
##########################
```
```PY
####### LineRegisterPrimary #######

from CyberTKAPI.api import API

phone = input("\nLutfen Numara Giriniz: ") #EXAMPLE; 628382302****, 90538765****
countryCode = input("Lutfen Ulke Kodu Giriniz: ") #EXAMPLE;  ID, TH, TR, US, NL
ip = input("Lutfen IP Giriniz: ") #EXAMPLE; Please write any ip address that belongs to the same location as the number you use.


apiKey = "LosAngeles"
version = "v2"

RegisterPrimary = API(apiKey,version)
registerPhone = RegisterPrimary.RegisterPrimary(phone,countryCode,ip)
RegisterPrimary.GoodPrint(registerPhone)

PinCode = int(input("\nLutfen Gelen Pinkodunu Giriniz: "))

registerPhoneResult = RegisterPrimary.RegisterPrimaryResult(phone,
countryCode,
ip,
registerPhone["Key"],
registerPhone["Session"],
PinCode)

RegisterPrimary.GoodPrint(registerPhoneResult)

##########################
```


  

LAST UPDATE: 03/02/2022


- LICENSE: Free;
- ApiKey ?: LosAngeles
- ?????? Bug Report Line ID: cybertk0 

- ???? Email, [email](mailto:tolgkr@cybertkr.com) ???
- ???? Whatsaap, [link](https://api.whatsapp.com/send?phone=31686208125)???

<a href="https://www.buymeacoffee.com/cybertkr" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>

