def get_initials(fullname):
    initial = fullname[0]
    found = False
    for letter in fullname:
        if found is True:
            initial = initial + letter
            found = False
        elif letter == " ":
            found = True
        else:
            initial = initial
    return initial.upper()

def main():
    fullname=input("What is your full name?")
    print(get_initials(fullname))

if __name__ == '__main__':
    main()
