# -*- coding: utf-8 -*-

from zipfile import ZipFile

class Autozip:

    trypwd = ""
    pwchr = ""

    def __init__(self, path="./resource/", zipfilename="Autoexec.zip"):
        self.path = path
        self.zipfilename = zipfilename


    def dicCrack(self, zip, pw):
        try:
            print(f"[+] Try password : {pw.decode()}")
            zip.extractall(pwd=pw)
            self.trypwd = pw.decode()
        except Exception as e:
            print(f"[-] Error log : {e}.")
        finally:
            return

    def run(self, dicFile="dic.txt"):

        print("Start CrackZip")
        f = open(self.path+dicFile, 'r')

        lines = f.readlines()

        with ZipFile(self.path+self.zipfilename, 'r') as zip:
            for line in lines:
                pwd = line.strip("\n")
                self.dicCrack(zip, pwd.encode("UTF-8"))

        f.close()

        return self.trypwd
