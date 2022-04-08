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