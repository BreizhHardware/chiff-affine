from crypt_and_decrypt import *
from find_key import *

cryptByteFile('../demo.mp3', 45, 85, '../demoCrypted.mp3')
print('Crypted')
decryptByteFile('../demoCrypted.mp3', 45, 85, '../demoDeCrypted.mp3')
print('Decrypted')