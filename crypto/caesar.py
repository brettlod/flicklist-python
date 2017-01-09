from sys import argv, exit
from helpers import alphabet_position, rotate_character

def encrypt(tex, rot):
    encrypted = ''
    rot=rot
    for char in tex:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            newChar = rotate_character(char, rot)
            encrypted = encrypted + newChar

    return encrypted

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False
    if cl_args[1].isdigit() is False:
        return False
    return True    

def main():
    if user_input_is_valid(argv) == False:
        print("usage: python3 caesar.py n")
        exit()
    messageRot=argv[1]
    messageTex=input("Type a message:")
    print(encrypt(messageTex, messageRot))

if __name__ == '__main__':
    main()
