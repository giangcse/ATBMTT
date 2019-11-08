from Crypto.PublicKey import RSA

key = RSA.generate(2048)
f = open('keyName.pem', 'wb')
f.write(key.exportKey('PEM'))
f.close()
