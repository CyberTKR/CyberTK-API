#!/usr/bin/python
# -*- coding: utf-8 -*-
import httpx,json,sys


class API:

    def __init__(self, ApiKey, Version):
        self._h = 'https://api.cybertkr.com'
        self._get = httpx.Client(http2=True, timeout=120)
        self.api_key = ApiKey
        self.api_version = Version
        self.api_versionFloat = "2.9"
        self.headers = {'ApiKey': self.api_key,'API-Version': self.api_version}
        self.CheckApiUpdate()

    def CheckApiUpdate(self):
        VersionCheck = self._get.get("https://raw.githubusercontent.com/CyberTKR/CyberTK-API/master/CyberTKAPI/__version__").text.replace("\n"," ").replace(" ","")
        if str(VersionCheck) != self.api_versionFloat:
            print("\n\nPlease update the API : https://github.com/CyberTKR/CyberTK-API/\n\n")
            sys.exit()
            
    def GoodPrint(self, jsonpack):
        print(json.dumps(jsonpack, indent=4,ensure_ascii=False))

    def _appuseragent(self, 
                      App):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/appname?App=' + App,
                               headers=self.headers).json()
        return istek

    def _apprandom(self):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/apprandom',
                               headers=self.headers).json()
        return istek

    def _weatherapi(self, location):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/weatherapi?Location=' + location,
                               headers=self.headers).json()
        return istek

    def _instaprofile(self, username):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/instagraminstasearch?Parameters='
                                + username, headers=self.headers).json()
        return istek

    def _screenShotWeb(self, query):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/webscreenshot?Parameters=' + query,
                               headers=self.headers)
        return istek

    def _covid19(self, countrycode):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/covid19api?Parameters='
                               + countrycode, headers=self.headers)
        return istek

    def _tiktoksearch(self, username):
        istek = self._get.post(self._h + '/' + self.api_version
                               + '/tiktokapi?Parameters=' + username,
                               headers=self.headers)
        return istek

    def _lineqr(self, appname, UserAgent):
        self.headers['AppName'] = appname
        self.headers['UserAgent'] = UserAgent
        istek = json.loads(self._get.post(self._h + '/'
                           + self.api_version + '/qrCode',
                           headers=self.headers).text)
        return istek

    def _linepin(
        self,
        key,
        session,
        appname,
        userAgent,
        ):
        self.headers['AppName'] = appname
        self.headers['UserAgent'] = userAgent
        istek = json.loads(self._get.post(self._h + '/'
                           + self.api_version + '/Pincode' + '/' + key
                           + '/' + session, headers=self.headers).text)
        return istek

    def _lineauthToken(
        self,
        key,
        session,
        appname,
        userAgent,
        ):
        self.headers['AppName'] = appname
        self.headers['UserAgent'] = userAgent
        istek = json.loads(self._get.post(self._h + '/'
                           + self.api_version + '/authToken' + '/'
                           + key + '/' + session,
                           headers=self.headers).text)
        return istek
    
    def _kicker(self,
        getJsonPostData: dict,
        ):
        GetJsonPostDatas = json.dumps(getJsonPostData)
        self.headers['Content-Type'] = 'application/json'
        istek = json.loads(self._get.post(self._h + '/'
                           + self.api_version + '/DeleteOtherFromChatALL',data=GetJsonPostDatas,
                           headers=self.headers).text)
        return istek
    
    def RegisterPrimary(self,phone,country,ip):
        self.headers['Phone'] = phone
        self.headers['CountryCode'] = country
        self.headers['IP'] = ip
        istek = json.loads(self._get.post(self._h + '/'
                           + self.api_version + '/LINE/RegisterPrimaryService',
                           headers=self.headers).text)
        if istek["Status"] != 200:
            raise Exception (istek["ErrorMessage"])
        return istek
    
    def RegisterPrimaryResult(self,phone,country,ip,key,session,pin):
        self.headers['Phone'] = phone
        self.headers['CountryCode'] = country
        self.headers['IP'] = ip
        istek = json.loads(self._get.post(self._h + '/' + self.api_version + '/LINE/RegisterPrimaryService/'+ key + '/' + session + '/' + str(pin),headers=self.headers).text)
        if istek["Status"] != 200:
            raise Exception (istek["ErrorMessage"])
        return istek
    
