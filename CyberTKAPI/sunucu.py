import aiohttp




class ApiSunucu(object):
    
    def __init__(self):
        self.Hcl58y0 = {}
        self.v291jqA = {}
        
        
    async def bR3k9c(self,X2Qjs62,n2AN4n,d6YJV4,Hcl58y0=None,v291jqA=None):
        
        Y1fqJ12 = aiohttp.ClientSession()
        async with Y1fqJ12 as xeLsT9E:
            y37ycKC = X2Qjs62+n2AN4n
            async with xeLsT9E.get(y37ycKC,headers=Hcl58y0, json=v291jqA) as E3k2Wi2:
                if d6YJV4 == "text":
                    return await E3k2Wi2.text()
                elif d6YJV4 == "json":
                    return await E3k2Wi2.json(content_type='application/json')