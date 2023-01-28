from .config import *
import aiohttp,asyncio,json



class CyberTKAPI(Config):
    
    def __init__(self):
        Config.__init__(self)
    
    async def CreateTransPortGet(self,host,endpoint,contentIn,reqHead=None,reqJson=None):
        
        aioClientSession = aiohttp.ClientSession()
        async with  aioClientSession as TransPortSession:
            ReqUrl = host+endpoint
            async with TransPortSession.get(ReqUrl,headers=reqHead, json=reqJson) as respon:
                if contentIn == "text":
                    return await respon.text()
                elif contentIn == "json":
                    return await respon.json(content_type='application/json')

    @staticmethod
    def apiPrint(prinText):
        print(prinText)
        
    @staticmethod
    def apiJsonPrint(prinText):
        print(json.dumps(prinText,indent=4))
        
        
        
    def lineQr(self):
        return asyncio.run(self.CreateTransPortGet(self.LINE_QR_HOST,"/link",contentIn="json"))
        
    def linePin(self,key):
        return asyncio.run(self.CreateTransPortGet(self.LINE_QR_HOST,f"/pincode/{key}",contentIn="json"))
    
    def lineToken(self,key):
        return asyncio.run(self.CreateTransPortGet(self.LINE_QR_HOST,f"/authToken/{key}",contentIn="json"))
    
    def lineLiff(self,token,appname,url):
        self.ReqJson["url"]= url
        self.ReqJson["token"] = token
        self.ReqJson["appname"]= appname
        self.ReqJson["Content-Type"] = 'application/json'
        print(self.ReqJson)
        return asyncio.run(self.CreateTransPortGet(self.LINE_LIFF_HOST,f"/liffapproval",contentIn="text",reqHead=self.ReqHead,reqJson=self.ReqJson))