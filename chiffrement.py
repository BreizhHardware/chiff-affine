#R = machin.read(1)
#if not R = \00
def pgcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def chiffrementAffine(a,b,L):
        alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        x=alphabet.index(L)
        y=(a*x+b)%26
        return alphabet[y]
def inverse(a):
        x=0
        while (a*x%26!=1):
                x=x+1
        return x
def dechiffrementAffine(a,b,L):
    alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    x=alphabet.index(L)
    y=(inverse(a)*(x-b))%26
    return alphabet[y]
                

def crypt(M,a,b):
    if (pgcd(a,26)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(chiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Chiffrement impossible. Veuillez choisir un nombre a premier avec 26."

def decrypt(M,a,b):
    if (pgcd(a,26)==1):
        mot = []
        for i in range(0,len(M)):
                mot.append(dechiffrementAffine(a,b,M[i]))
        return "".join(mot)
    else:
        return "Déchiffrement impossible. Le nombre a n'est pas premier avec 26."
def readByteFile(A: str):
    with open(A, "rb") as f:
        with open("result.txt", "a+") as o:
            byte = f.read(1)
            while (byte := f.read(1)):
                o.write(str(byte))
def decouper(F: str):
    fd = open("result.txt", "r").readlines()
    for line in fd:
        line = line.sp

        
def cryptFichier(A: str, a,b):
    X = openBytesFile(A)
    fdout = open("resulttest.txt", "wb")
    for i in range(len(X)):
        fdout.write(X[i])
    crypt(fdout, a, b)

def openBytesFile(A: str):
    opened = []
    fdin = open(A, "rb")
    data = fdin.read(1)
    while data != b'':
        opened.append(data)
        data = fdin.read(1)
    fdin.close()
    return opened

print(chiffrementAffine(1, 3, 'P'))
print(crypt("JAIMELESFRITESALAFRITEUSES", 1, 3))
print(openBytesFile("testcrypt.txt"))
