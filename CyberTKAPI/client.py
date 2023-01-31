import asyncio,json
from .sunucu import *
from .ayarlar import *



class CyberTKAPI(Ayarlar,ApiSunucu):
    
    def __init__(self):
        Ayarlar.__init__(self)
        ApiSunucu.__init__(self)

    @staticmethod
    def apiPrint(G5QweT):
        print(G5QweT)
        
    @staticmethod
    def apiJsonPrint(qb9LNE: dict):
        print(json.dumps(qb9LNE,indent=4))
        
    def lineQr(self):
        return asyncio.run(self.bR3k9c(self.LINE_QR_HOST,self.LINE_QR_ENDPOINT,d6YJV4="json"))
        
    def linePin(self,xqxY4r):
        return asyncio.run(self.bR3k9c(self.LINE_QR_HOST,self.LINE_PINCODE_ENDPOINT + f"/{xqxY4r}",d6YJV4="json"))
    
    def lineToken(self,xqxY4r):
        return asyncio.run(self.bR3k9c(self.LINE_QR_HOST,self.LINE_ATOKEN_ENDPOINT + f"/{xqxY4r}",d6YJV4="json"))
    
    def lineLiff(self,token,appname,url):
        self.v291jqA["url"]= url
        self.v291jqA["token"] = token
        self.v291jqA["appname"]= appname
        self.Hcl58y0["Content-Type"] = 'application/json'
        return asyncio.run(
            self.bR3k9c(
                self.LINE_LIFF_HOST,
                self.LINE_LIFF_ENDPOINT,
                d6YJV4="text",
                Hcl58y0=self.Hcl58y0,
                v291jqA=self.v291jqA
            ))