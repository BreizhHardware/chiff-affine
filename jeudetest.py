from crypt_and_decrypt import *
from find_key import *



#print(sortbyteFreq(byteFreq("data")))
#findKeywrite(b'\xaa', b'\x20', "keyoutspace")
#findKeywrite(b'\x31', b'\x65', "keyoute")
#print(findKeyList(b'\xaa', b'\x20'))
#print(comparKey(findKeyList(b'\xaa', b'\x20'), findKeyList(b'\x31', b'\x65')))
#cryptByteFile('tescrypt.txt', 1, 3, "resulttest2")
#cryptByteFile('data', 1, 3, 'resultcryptdata')
#cryptByteFile('monkey.jpg', 1, 3)
#decryptByteFile('resulttest2', 1, 3, "decryptresult2")
#decryptByteFile('resultcryptdata', 1, 3, 'resultdecryptdata')
decryptByteFile('data', 
                comparKey(findKeyList(b'\xaa', b'\x20'), findKeyList(b'\x31', b'\x65'))[0],
                comparKey(findKeyList(b'\xaa', b'\x20'), findKeyList(b'\x31', b'\x65'))[1], 
                "dataDecrypted")
#cryptByteFile('enemy-from-the-series-arcane-league-of-legends.mp3', 45, 76, 'enemyCrypted')
#decryptByteFile('enemyCrypted', 45, 76, 'enemyDeCyted.mp3')
