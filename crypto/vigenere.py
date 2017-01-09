from helpers import alphabet_position, rotate_character

def encrypt(tex, key):
    keyIndex=0
    keyLength=len(key)
    encrypted = ''
    for char in tex:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            if keyIndex < keyLength:
                keyText=key[keyIndex]
                KeyRot=alphabet_position(keyText)
                keyIndex=keyIndex+1
            else:
                keyText=key[0]
                KeyRot=alphabet_position(keyText)
                keyIndex=1

            newChar = rotate_character(char, KeyRot)
            encrypted = encrypted + newChar

    return encrypted

def main():
    messageTex=input("Type a message:")
    messageRot=input("Encryption key:")
    print(encrypt(messageTex, messageRot))

if __name__ == '__main__':
    main()
