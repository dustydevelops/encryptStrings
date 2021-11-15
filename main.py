
from cryptography.fernet import Fernet
 
# we will be encryting the below string.
message = "no one will be able to guess this"
 
#this key will allow us to access the encrypted data later.
key = Fernet.generate_key()
print(key) 
 
# execute encryption using the Fernet class and key
fernet = Fernet(key)
encMessage = fernet.encrypt(message.encode())
 
#print the encrypted message
print("encrypted string: ", encMessage)
 
#decrypt the message
decMessage = fernet.decrypt(encMessage).decode()
 
#print the decrypted string
print("decrypted string: ", decMessage)
