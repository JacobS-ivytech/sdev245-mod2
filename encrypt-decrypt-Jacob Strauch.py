#Script to demonstrate basic symmetric and asymmetric encryption
from cryptography.fernet import Fernet
import rsa

#message to encrypt
ogMessage = "I would have lived in peace. But my enemies brought me war."


#Symetric key generation
secretKey = Fernet.generate_key()

#instance fernet class
fernet = Fernet(secretKey)

#encrypt message with secret key
encMessageSym = fernet.encrypt(ogMessage.encode())

#decrypt message with secret key
decMessageSym = fernet.decrypt(encMessageSym).decode()

#print each step from symmetric encryption
print("Orignial message: ", ogMessage)
print("Secret Key: ", secretKey)
print("Symmetric encrypted string: ", encMessageSym)
print("Decrypted Symmetric string: ", decMessageSym)


#generate asymmetric key pair
publicKey, privateKey = rsa.newkeys(650)

#encrypt message with public key
encMessageAsym = rsa.encrypt(ogMessage.encode(), publicKey)

#decrypt message with private key
decMessageAsym = rsa.decrypt(encMessageAsym, privateKey).decode()

#print each piece of asymmetric encryption
print("\nOrignial message: ", ogMessage)
print("Public Key: ", publicKey)
print("Private Key: ", privateKey)
print("Asymmetric encrypted string: ", encMessageAsym)
print("Decrypted Asymmetric string: ", decMessageAsym)
