# The Henry Cipher, Created by Henry Price on 3/11/19
# All rights reserved

import random


def cipher2(inmsg, keysplit1, keysplit2, key):

    startmsg = inmsg
    msglist = list(startmsg)
    key = key
    bigout = ""
    x = 0

    try:
        for i in msglist:

            keysplit = int(keysplit1)

            output = (ord(msglist[x])) * (int(key[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key1 = key[keysplit:]
            key1 = key1 + key[0:keysplit]

            keysplit = int(keysplit2)

            output = (ord(msglist[x])) * (int(key1[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

    except IndexError:
        return bigout


def cipher3(inmsg, keysplit1, keysplit2, keysplit3, key):

    startmsg = inmsg
    msglist = list(startmsg)
    key = key
    bigout = ""
    x = 0

    try:
        for i in msglist:

            keysplit = int(keysplit1)

            output = (ord(msglist[x])) * (int(key[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key1 = key[keysplit:]
            key1 = key1 + key[0:keysplit]

            keysplit = int(keysplit2)

            output = (ord(msglist[x])) * (int(key1[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key2 = key1[keysplit:]
            key2 = key2 + key[0:keysplit]

            keysplit = int(keysplit3)

            output = (ord(msglist[x])) * (int(key2[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

    except IndexError:
        return bigout


def cipher4(inmsg, keysplit1, keysplit2, keysplit3, keysplit4, key):

    startmsg = inmsg
    msglist = list(startmsg)
    key = key
    bigout = ""
    x = 0

    try:
        for i in msglist:

            keysplit = int(keysplit1)

            output = (ord(msglist[x])) * (int(key[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key1 = key[keysplit:]
            key1 = key1 + key[0:keysplit]

            keysplit = int(keysplit2)

            output = (ord(msglist[x])) * (int(key1[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key2 = key1[keysplit:]
            key2 = key2 + key[0:keysplit]

            keysplit = int(keysplit3)

            output = (ord(msglist[x])) * (int(key2[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

            key3 = key2[keysplit:]
            key3 = key3 + key[0:keysplit]

            keysplit = int(keysplit4)

            output = (ord(msglist[x])) * (int(key3[0:keysplit]))
            # print(output, end=' ')
            bigout = str(bigout) + " " + str(output)
            x += 1

    except IndexError:
        return bigout


def randkey(keylen):
    keylength = keylen
    keyout = ""
    for i in range(int(keylength)):
        output = random.randrange(1,9)
        keyout = keyout + str(output)
    print("Your key is: " + keyout)
    return keyout


def start(emsg):
    pattern = input("Keysplit pattern: ")
    pattern = pattern.split(" ")
    keypatt = 0

    for x in range(len(pattern)):
        keypatt = keypatt + int(pattern[x])

    if len(pattern) == 2:
        key = input("Key: ")
        if key == "Random" or "random":
            key = randkey(keypatt)
            # user = input("Msg: ")
            return cipher2(inmsg=emsg, keysplit1=pattern[0], keysplit2=pattern[1], key=key)
        else:
            # user = input("Msg: ")
            return cipher2(inmsg=emsg, keysplit1=pattern[0], keysplit2=pattern[1], key=key)

    if len(pattern) == 3:
        key = input("Key: ")
        if key == "Random" or "random":
            key = randkey(keypatt)
            # user = input("Msg: ")
            return cipher3(inmsg=emsg, keysplit1=pattern[0], keysplit2=pattern[1], keysplit3=pattern[2], key=key)
        else:
            # user = input("Msg: ")
            return cipher3(inmsg=emsg, keysplit1=pattern[0], keysplit2=pattern[1], keysplit3=pattern[2], key=key)

    if len(pattern) == 4:
        key = input("Key: ")
        if key == "Random" or "random":
            key = randkey(keypatt)
            # user = input("Msg: ")
            return cipher4(inmsg=emsg,
                           keysplit1=pattern[0],
                           keysplit2=pattern[1],
                           keysplit3=pattern[2],
                           keysplit4=pattern[3],
                           key=key)

        else:
            # user = input("Msg: ")
            return cipher4(inmsg=emsg,
                           keysplit1=pattern[0],
                           keysplit2=pattern[1],
                           keysplit3=pattern[2],
                           keysplit4=pattern[3],
                           key=key)

    else:
        print("Sorry, this is not currently supported")


if __name__ == '__main__':
    user = input("Msg: ")
    print(start(emsg=user))
