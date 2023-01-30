from .ayarlar import *
import aiohttp,asyncio,json



class CyberTKAPI(Ayarlar):
    
    def __init__(self):
        Ayarlar.__init__(self)
    
    async def bR3k9c(self,X2Qjs62,n2AN4n,d6YJV4,Hcl58y0=None,v291jqA=None):
        
        Y1fqJ12 = aiohttp.ClientSession()
        async with Y1fqJ12 as TransPortSession:
            ReqUrl = X2Qjs62+n2AN4n
            async with TransPortSession.get(ReqUrl,headers=Hcl58y0, json=v291jqA) as E3k2Wi2:
                if d6YJV4 == "text":
                    return await E3k2Wi2.text()
                elif d6YJV4 == "json":
                    return await E3k2Wi2.json(content_type='application/json')

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
        self.v291jqA["Content-Type"] = 'application/json'
        return asyncio.run(
            self.bR3k9c(
                self.LINE_LIFF_HOST,
                self.LINE_LIFF_ENDPOINT,
                d6YJV4="text",
                Hcl58y0=self.Hcl58y0,
                v291jqA=self.v291jqA
            ))