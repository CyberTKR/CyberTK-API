`ApiFun &*`
 
`Example For API ;`




- Line QR


```PY
from CyberTKAPI import *

# QR
xbGs2q = CyberTKAPI()
kY5tSP = xbGs2q.lineQr()
xbGs2q.apiJsonPrint(kY5tSP)

# Pincode
dv5KZW = kY5tSP["Key"]
q5LjKf = xbGs2q.linePin(dv5KZW)
xbGs2q.apiJsonPrint(q5LjKf)

# Token
w8YNrA = xbGs2q.lineToken(dv5KZW)
xbGs2q.apiJsonPrint(w8YNrA)
```



- Line LIFF
```PY

xqN5qj = xbGs2q.lineLiff("Token","App","consenturl")

xbGs2q.apiPrint(xqN5qj) #Response Text == 200: Success !
```

