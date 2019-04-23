# The deciphering tool to the Henry Cipher


def decipher2(inmsg, keysplit1, keysplit2, key):

    msg = inmsg
    msg = msg.split(' ')
    key = key
    bigout = ''
    x = 0

    try:
        for i in msg:
            try:

                keysplit = int(keysplit1)  # Sets the keysplit to 0 for when the program loops over

                output = chr(int(int(msg[x])/int(key[0:keysplit])))  # Math for deciphering message
                bigout = str(bigout) + str(output)

                #  This block of code creates the key split and sets the key to it's second state
                key1 = key[keysplit:]
                key1 = key1 + key[0:keysplit]
                keysplit = int(keysplit2)

                x += 1

                output = chr(int(int(msg[x])/int(key1[0:keysplit])))  # Math for deciphering the message
                bigout = str(bigout) + str(output)

                x += 1

            except ValueError:
                return bigout

    except IndexError:
        return bigout


def decipher3(inmsg, keysplit1, keysplit2, keysplit3, key):

    msg = inmsg
    msg = msg.split(' ')
    key = key
    bigout = ''
    x = 0

    try:
        for i in msg:
            try:

                keysplit = int(keysplit1)  # Sets the keysplit to 0 for when the program loops over

                output = chr(int(int(msg[x])/int(key[0:keysplit])))  # Math for deciphering message
                bigout = str(bigout) + str(output)

                #  This block of code creates the key split and sets the key to it's second state
                key1 = key[keysplit:]
                key1 = key1 + key[0:keysplit]
                keysplit = int(keysplit2)

                x += 1

                output = chr(int(int(msg[x])/int(key1[0:keysplit])))  # Math for deciphering the message
                bigout = str(bigout) + str(output)

                x += 1

                key2 = key1[keysplit:]
                key2 = key2 + key[0:keysplit]

                keysplit = int(keysplit3)

                output = chr(int((int(msg[x])) / (int(key2[0:keysplit]))))
                bigout = str(bigout) + str(output)
                x += 1

            except ValueError:
                return bigout

    except IndexError:
        return bigout


def decipher4(inmsg, keysplit1, keysplit2, keysplit3, keysplit4, key):

    msg = inmsg
    msg = msg.split(' ')
    key = key
    bigout = ''
    x = 0

    try:
        for i in msg:
            try:

                keysplit = int(keysplit1)  # Sets the keysplit to 0 for when the program loops over

                output = chr(int(int(msg[x])/int(key[0:keysplit])))  # Math for deciphering message
                bigout = str(bigout) + str(output)

                #  This block of code creates the key split and sets the key to it's second state
                key1 = key[keysplit:]
                key1 = key1 + key[0:keysplit]
                keysplit = int(keysplit2)

                x += 1

                output = chr(int(int(msg[x])/int(key1[0:keysplit])))  # Math for deciphering the message
                bigout = str(bigout) + str(output)

                x += 1

                key2 = key1[keysplit:]
                key2 = key2 + key[0:keysplit]

                keysplit = int(keysplit3)

                output = chr(int((int(msg[x])) / (int(key2[0:keysplit]))))
                bigout = str(bigout) + str(output)
                x += 1

                key3 = key2[keysplit:]
                key3 = key3 + key[0:keysplit]

                keysplit = int(keysplit4)

                output = chr(int((int(msg[x])) / (int(key3[0:keysplit]))))
                bigout = str(bigout) + str(output)
                x += 1

            except ValueError:
                return bigout

    except IndexError:
        return bigout


def start(imsg):
    pattern = input("Keysplit pattern: ")
    pattern = pattern.split(" ")

    if len(pattern) == 2:
        # user = input("Msg: ")
        key = input("Key: ")
        return (decipher2(inmsg=imsg, keysplit1=pattern[0], keysplit2=pattern[1], key=key))

    if len(pattern) == 3:
        # user = input("Msg: ")
        key = input("Key: ")
        return (decipher3(inmsg=imsg, keysplit1=pattern[0], keysplit2=pattern[1], keysplit3=pattern[2], key=key))

    if len(pattern) == 4:
        # user = input("Msg: ")
        key = input("Key: ")
        return (decipher4(inmsg=imsg,
                        keysplit1=pattern[0],
                        keysplit2=pattern[1],
                        keysplit3=pattern[2],
                        keysplit4=pattern[3],
                        key=key))

    else:
        print("Sorry not supported ")


if __name__ == '__main__':
    user = input("Msg: ")
    print(start(imsg=user))
