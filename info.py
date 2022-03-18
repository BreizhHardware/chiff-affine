def brutforce(filenameIn: str, filenameOut = 'result'):
    maj = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    createFile(filenameOut)
    fdin = open(filenameIn, "rb")
    fdout = open(filenameOut, "wb")
    data = fdin.read(1)
    for keya in range(1, 256):
        print(keya)
        for keyb in range(1, 256):
            print(keyb)
            i = dechiffrementAffineByte(data, keya, keyb)
            ib = str(i, "utf-8")
            for ib in maj:
                fdout.write(i)

def findKey(data: bytes, dataout: bytes, filenameOut = 'result'):
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