from string import *
import pickle as p
from time import sleep 


def write(filepath):
    msg = input("Enter message: ")
    with open(filepath, 'wb+') as fh:
        p.dump(msg, fh)


def crack(filepath):
    all = ascii_letters + digits + ' ' + punctuation

    with open(filepath, 'rb') as fh:
        fh.seek(0)
        password = p.load(fh)

    cur = []
    for i in range(len(password)):
        for j in all:
            try:
                cur[i]=j
            except:
                cur.append(j)

            sleep(0.01)
            print(''.join(cur))
            if j==password[i]:
                break

    print(password)


#__main__
ch=int(input("1. Write\n2. Crack\n\nEnter choice: "))

if ch==1:
    filepath=input("Enter file path: ")
    write(filepath)
elif ch==2:
    filepath=input("Enter file path: ")
    crack(filepath)
else:
    exit()