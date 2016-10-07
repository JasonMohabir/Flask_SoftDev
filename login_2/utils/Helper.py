import hashlib
import csv

def CSVtoDict(filepath):
    with open(filepath , 'rb') as f:
        reader = csv.reader(f)
        mydict = dict(reader)
    return mydict

def addUser(filepath, user, pword):
     with open(filepath,'a') as f:
        w = csv.writer(f)
        w.writerow([user, createHash(pword)])

def createHash(pword):
    hashPass = hashlib.sha1()
    hashPass.update(pword)
    return hashPass.hexdigest()
    


def isMatch(pword, givenPass):
    return pword == createHash(givenPass)


