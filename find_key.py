from crypt_and_decrypt import *

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
    """Ecrit dans filenameOut les couples de clé possible pour que data soit égale à dataout.
    """
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
    """Renvoie la liste des couples de clé possible pour que data soit égale à dataout.
    """
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
    """Compare les couples de clé valeur et renvoie le couple commun aux 2 listes M et L.
    """
    for i in range(len(L)):
        for y in range(len(M)):
            if L[i] == M[y]:
                return L[i]
                