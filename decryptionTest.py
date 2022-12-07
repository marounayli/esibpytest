from cryptography.fernet import Fernet
import secretKey
import json
import identity
import base64
import os


s = "gAAAAABjkIjqkBOLJsD18TQ_4hz_Sgiq9qNlc3FTjHiKvzX-f3d9CuSaGOHokmAGdtWdw878QVHLCdRXZCEYquzPL048s5mJI3YwkC6odqcFEcWArWilrds="

fernet = Fernet(secretKey.key)

decrypted_str = fernet.decrypt(s.encode())

d = json.loads(decrypted_str)

print(d)
