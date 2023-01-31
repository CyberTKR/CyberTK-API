from CyberTKAPI import *



############## Line QR ##############

# QR
xbGs2q = CyberTKAPI()
kY5tSP = xbGs2q.lineQr("IOSIPAD") #IOSIPAD, DESKTOPMAC, DESKTOPWIN, CHROMEOS
xbGs2q.apiJsonPrint(kY5tSP)

# Pincode
dv5KZW = kY5tSP["Key"]
q5LjKf = xbGs2q.linePin(dv5KZW)
xbGs2q.apiJsonPrint(q5LjKf)

# Token
w8YNrA = xbGs2q.lineToken(dv5KZW)
xbGs2q.apiJsonPrint(w8YNrA)




############## Line LIFF ##############

xqN5qj = xbGs2q.lineLiff("Token","AppName","consenturl") # AppName Example "DESKTOPMAC/t7.12.0/tMAC/t13.0"

xbGs2q.apiPrint(xqN5qj) #Response Text == 200: Success !