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
    x = alphabet.index(int.from_bytes(data, "little"))
    y = (keya*x+keyb)%256
    return bytes([alphabet[y]])


def inverse(a):
    """ Renvoie l'inverse du module de a et x par 256
    """
    x = 0
    while (a*x%256 != 1):
            x += 1
    return x


def dechiffrementAffineByte(data: bytes, keya: int, keyb: int) -> bytes:
    """ Renvoie le byte data décrypté avec le chiffrement affine
    """
    alphabet = []
    for i in range(256):
        alphabet.append(i)
    x = alphabet.index(int.from_bytes(data, "little"))
    y = (inverse(keya)*(x-keyb))%256
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