# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64

import random, string
def randomword(length):
   letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
   return ''.join(random.choice(letters) for i in range(length))


if (False):
    input_txt = 'test some plain text here'

    msg_text = input_txt.rjust(64)
    
    encoded = base64.b64encode(cipher.encrypt(msg_text))
    
    decoded = cipher.decrypt(base64.b64decode(encoded))
    
    print("Secret message is : ", input_txt)
    print('Secret Key is : ', secret_key)
    print('-'*60)
    print('Encrypted message is : ', encoded)
    print('-'*60)
    print('DeCrypted message is : ', decoded)
    print('Pretty print DeCrypted message : ', decoded.strip().decode("utf-8"))
    print('-'*60)

#----------------------------------------

#secret_key = randomword(32)
secret_key = '7dSzTnFl9Miyr2OGh38U2tmaqGmXhZV1'

cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously

#convert to bytes
#usr = "6432761ziet" 
#usr = b"user_ID\n" #or usr = "user_ID\n".encode()
#input_string = "user_ID"
input_string = ['user_ID','yroliK darnoC','user_Password','drwssp_ym'] 


usr = [(x + "\n").rjust(16).encode() for x in input_string if(True)]
#usr = usr.rjust(16)
#usr = usr.encode()
print(usr)

encoded = [base64.b64encode(cipher.encrypt(x)) for x in usr if (True)]
#encoded = base64.b64encode(cipher.encrypt(usr))

#save to txt file
with open("my_text.txt", "wb") as f:
    #f.write(usr)
    #f.write(encoded)
    #[f.write(x) for x in encoded if (True) ]
    for x in encoded:
        f.write(x)
        f.write("\n".rjust(16).encode())
    f.close()
#in_file = open("my_text.txt", "rb") # opening for [r]eading as [b]inary
#data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
#in_file.close()

#open txt file
with open("my_text.txt", "rb") as f:
    content = f.readlines()
    f.close()
content = [x.strip() for x in content] 
print(content)

decoded = cipher.decrypt(base64.b64decode(content[0]))
output_string = str(decoded.strip())[2:-1]
print(output_string)


for x in content:
    decoded = cipher.decrypt(base64.b64decode(x))
    output_string = str(decoded.strip())[2:-1]
    print(output_string)

    

#########################################
    

def crypt(theaction, my_object):
    #if (theaction == 'encrypt' & isinstance(my_object, str)):
    secret_key = '1234567890123456'
    cipher = AES.new(secret_key,AES.MODE_ECB)
    
    if (theaction == 'encrypt'):
        my_object = my_object.rjust(32)
        my_encrypt = base64.b64encode(cipher.encrypt(my_object))
        return my_encrypt
    
 #   elif (theaction == 'decrypt' & isinstance(my_object, (bytes, bytearray))):
    elif (theaction == 'decrypt'):
        my_decrypt = cipher.decrypt(base64.b64decode(my_object))
        return my_decrypt.strip().decode("utf-8")
