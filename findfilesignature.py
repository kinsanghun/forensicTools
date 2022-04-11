class findFileSignature:
    def __init__(self, path="./resource/"):
        self.path = path

    def find(self, filename):
        file = open(self.path + filename, 'rb')
        magic = file.read(16)

        return magic.hex()

    def whatisfileextension(self, filename):
        sig = self.find(filename)
        res = list()
        with open(self.path + "signature_format.txt", "r") as f:
            datas = f.readlines()

            for data in datas:
                tmp = data.strip("\n").split("$")
                if sig[:len(tmp[1])].upper() == tmp[1].upper():
                    res.append(tmp)

            return res

    def printExtensionList(self, extlist):
        for i, data in enumerate(extlist):
            print(i, data[0], data[1], data[2])
            print()