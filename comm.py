from string import *
import pickle as p
from time import sleep 


def write():
    msg = input("Enter message: ")
    with open('message', 'wb+') as fh:
        p.dump(msg, fh)


def crack():
    all = ascii_letters + digits + ' ' + punctuation

    with open('message', 'rb') as fh:
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
    write()
elif ch==2:
    crack()
else:
    exit()