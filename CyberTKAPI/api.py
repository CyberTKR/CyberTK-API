E='UserAgent'
D='AppName'
A='/'
import httpx,json as C
class API:
	def __init__(A,ApiKey,Version):A._h='https://app.cybertkr.com';A._get=httpx.Client(http2=True,timeout=120);A.api_key=ApiKey;A.api_version=Version;A.headers={'ApiKey':A.api_key,'API-Version':A.api_version}
	def GoodPrint(A,jsonpack):print(C.dumps(jsonpack,indent=4))
	def _appuseragent(B,App):C=B._get.post(B._h+A+B.api_version+'/appname?App='+App,headers=B.headers).json();return C
	def _apprandom(B):C=B._get.post(B._h+A+B.api_version+'/apprandom',headers=B.headers).json();return C
	def _weatherapi(B,location):C=B._get.post(B._h+A+B.api_version+'/weatherapi?Location='+location,headers=B.headers).json();return C
	def _instaprofile(B,username):C=B._get.post(B._h+A+B.api_version+'/instagramapi/instasearch?Parameters='+username,headers=B.headers).json();return C
	def _screenShotWeb(B,query):C=B._get.post(B._h+A+B.api_version+'/webscreenshot?Parameters='+query,headers=B.headers);return C
	def _covid19(B,countrycode):C=B._get.post(B._h+A+B.api_version+'/covid19api?Parameters='+countrycode,headers=B.headers);return C
	def _tiktoksearch(B,username):C=B._get.post(B._h+A+B.api_version+'/tiktokapi?Parameters='+username,headers=B.headers);return C
	def _lineqr(B,appname,UserAgent):B.headers[D]=appname;B.headers[E]=UserAgent;F=C.loads(B._get.post(B._h+A+B.api_version+'/qrCode',headers=B.headers).text);return F
	def _linepin(B,key,session,appname,userAgent):B.headers[D]=appname;B.headers[E]=userAgent;F=C.loads(B._get.post(B._h+A+B.api_version+'/Pincode'+A+key+A+session,headers=B.headers).text);return F
	def _lineauthToken(B,key,session,appname,userAgent):B.headers[D]=appname;B.headers[E]=userAgent;F=C.loads(B._get.post(B._h+A+B.api_version+'/authToken'+A+key+A+session,headers=B.headers).text);return F
