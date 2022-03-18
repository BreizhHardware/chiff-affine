def createFile(filename: str) -> None:
    """ Créer le fichier si il n'existe pas
    """
    try:
        with open(filename, 'x') as f:
            f.write('')
    except FileExistsError:
        return None


def cryptByteFile(filenameIn: str, keya: int, keyb: int, filenameOut = 'result') -> None:
    """ Ecrit dans filenameOut, filenameIn crypté avec le chiffrement affine
    """
    createFile(filenameOut)
    fdin = open(filenameIn, "rb")
    fdout = open(filenameOut, "wb")
    data = fdin.read(1)
    while data != b'':
        fdout.write(chiffrementAffineByte(data, keya, keyb))
        data = fdin.read(1)
    fdin.close()
    fdout.close()


def chiffrementAffineByte(data: bytes, keya: int, keyb: int) -> bytes:
    """ Renvoie le byte data crypté avec le chiffrement affine
    """
    alphabet = []
    for i in range(256):
        alphabet.append(i)
    x=alphabet.index(int.from_bytes(data, "little"))
    y=(keya*x+keyb)%256
    return bytes([alphabet[y]])

def inverse(a):
    """ Renvoie l'inverse du module de a et x par 256
    """
    x=0
    while (a*x%256 != 1):
            x += 1
    return x

def dechiffrementAffineByte(data: bytes, keya: int, keyb: int) -> bytes:
    """ Renvoie le byte data décrypté avec le chiffrement affine
    """
    alphabet = []
    for i in range(256):
        alphabet.append(i)
    x=alphabet.index(int.from_bytes(data, "little"))
    y=(inverse(keya)*(x-keyb))%256
    return bytes([alphabet[y]])
    

def decryptByteFile(filenameIn: str, keya: int, keyb: int, filenameOut = 'result') -> None:
    """ Ecrit dans filenameOut, filenameIn décrypté avec le chiffrement affine
    """
    createFile(filenameOut)
    fdin = open(filenameIn, "rb")
    fdout = open(filenameOut, "wb")
    data = fdin.read(1)
    while data != b'':
        fdout.write(dechiffrementAffineByte(data, keya, keyb))
        data = fdin.read(1)
    fdin.close()
    fdout.close()


def byteFreq(filenameIn: str) -> dict:
    """ byteDict est un dictionnaire tel que
            * une clé est un octet
            * la valeur associée est la fréquence de ce octet.
            
        Met à jour byteDict avec la liste de octets lbyte.
    """
    lbyte = []
    byteDict = {}
    fdin = open(filenameIn, "rb")
    data = fdin.read(1)
    while data != b'':
        lbyte.append(data)
        data = fdin.read(1)
    for octet in lbyte:
        if octet in byteDict:
            freq = byteDict[octet] + 1
        else:
            freq = 1
        byteDict[octet] = freq
    return byteDict


def sortbyteFreq(byteFreq : dict) -> list:
    """ Renvoie la liste de couples (octet, freq) de byteFreq.
        Les couples sont triés par ordre décroissant de freq.
    """
    byteList = [(octet, byteFreq[octet]) for octet in byteFreq]
    k = 1
    while k < len(byteList):
        i = k
        while i > 0 and byteList[i - 1][1] < byteList[i][1]:
            byteList[i - 1], byteList[i] = byteList[i], byteList[i - 1] 
            i = i - 1  
        k = k + 1
    return byteList


def findKeywrite(data: bytes, dataout: bytes, filenameOut = 'result'):
    createFile(filenameOut)
    fdout = open(filenameOut, "w")
    for keya in range(1, 256):
        if keya % 2 != 0:
            for keyb in range(1, 256):
                i = dechiffrementAffineByte(data, keya, keyb)
                if i == dataout:
                    fdout.write("keya: ")
                    fdout.write(str(keya))
                    fdout.write(" ")
                    fdout.write("keyb: ")
                    fdout.write(str(keyb))
                    fdout.write("\n")

def findKeyList(data: bytes, dataout: bytes):
    L = []
    for keya in range(1, 256):
        if keya % 2 != 0:
            for keyb in range(1, 256):
                i = dechiffrementAffineByte(data, keya, keyb)
                if i == dataout:
                    t = (keya, keyb)
                    L.append(t)
    return L

def comparKey(L: list, M: list) -> tuple:
    for i in range(len(L)):
        for y in range(len(M)):
            if L[i] == M[y]: 
                return L[i]

#Jeu de test


#print(sortbyteFreq(byteFreq("data")))
#findKeywrite(b'\xaa', b'\x20', "keyoutspace")
#findKeywrite(b'\x31', b'\x65', "keyoute")
#print(findKeyList(b'\xaa', b'\x20'))
print(comparKey(findKeyList(b'\xaa', b'\x20'), findKeyList(b'\x31', b'\x65')))
#cryptByteFile('tescrypt.txt', 1, 3, "resulttest2")
#cryptByteFile('data', 1, 3, 'resultcryptdata')
#cryptByteFile('monkey.jpg', 1, 3)
#decryptByteFile('resulttest2', 1, 3, "decryptresult2")
#decryptByteFile('resultcryptdata', 1, 3, 'resultdecryptdata')
decryptByteFile('data', 91, 74, "decrptdatatest")
#cryptByteFile('enemy-from-the-series-arcane-league-of-legends.mp3', 45, 76, 'enemyCrypted')
#decryptByteFile('enemyCrypted', 45, 76, 'enemyDeCyted.mp3')


#nmb d'octet de e et code (b'x65')
#nmb d'octet de espace et code (b'x20')
#nmb d'octet de . et code (b'x2e')

# \x20 -> \xaa