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
    while (a*x%256!=1):
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


def brutforce(filenameIn: str, filenameOut = 'result'):
    maj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    createFile(filenameOut)
    fdin = open(filenameIn, "rb")
    fdout = open(filenameOut, "wb")
    data = fdin.read(1)
    for keya in range(256):
        print(keya)
        for keyb in range(256):
            print(keyb)
            i = dechiffrementAffineByte(data, keya, keyb)
            for i in maj:
                fdout.write(i)

#Jeu de test


#cryptByteFile('tescrypt.txt', 1, 3, "resulttest2")
#cryptByteFile('data', 1, 3, 'resultcryptdata')
#cryptByteFile('monkey.jpg', 1, 3)
#decryptByteFile('resulttest2', 1, 3, "decryptresult2")
#decryptByteFile('resultcryptdata', 1, 3, 'resultdecryptdata')
#decryptByteFile('result', 1, 3, "decryptmonkey.jpg")
#cryptByteFile('enemy-from-the-series-arcane-league-of-legends.mp3', 45, 76, 'enemyCrypted')
#decryptByteFile('enemyCrypted', 45, 76, 'enemyDeCyted.mp3')
brutforce('data')


#nmb d'octet de e et code (b'x65')
#nmb d'octet de s et code (b'x73')
#nmb d'octet de espace et code (b'x20')