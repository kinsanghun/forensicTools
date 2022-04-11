# -*- coding: utf-8 -*-

from autozip import Autozip
from findfilesignature import findFileSignature
from crawling_signature import crawling_signature
from imageGPS import imageinfo

RESOURCE_PATH = "./resource/"

def main():
    print("포렌식 분석 프로그램 Ver 1.0")
    filename = "Autoexec1.zip"

    print("Quit the program with Ctrl + C !!")
    while True:
        print("0. Update File Signature, 1. Print file signature, 2. Find zip password, 3. Find Image GPS ")
        selected = int(input("Select Menu : "))

        if selected == 0:
            crawling_signature()

        elif selected == 1:
            fs = findFileSignature()
            filesignature = fs.find(filename)
            fileextension = fs.whatisfileextension(filename)
            print(f"[!] File Signature is {filesignature}\n")
            fs.printExtensionList(fileextension)

        elif selected == 2:
            czip = Autozip(zipfilename=filename)
            print(f"\n[!] FIND PASSWORD : {czip.run()}\n")

        elif selected == 3:
            c = imageinfo()
            c.ImageGPS("img.JPG")

        else:
            print("[-] Undeveloped or invalid index number.")

if __name__ == "__main__":
    main()