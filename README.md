# sdev245-mod2
For this assignment we were to use symmetric and asymmetric encryption in a script to encode a short message. In order to accomplish this, I used two libraries with built-in functionality to create and implement the keys.

In symmetric encryption a single secret key is used by both the sender and receiver of the message. For this portion I imported Fernet from cryptography. With this library I could generate a secret key to encode and then decode a message. My program displays all relevant parts of this process in the console.

In asymmetric encryption a key pair is used to encode and decode a message. I used the rsa library to generate and implement my public and private keys for this portion. All components for this section are also printed to the console upon completion.

A screenshot displaying all components of both processes is included along with the original script.
