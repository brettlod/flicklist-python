#sentence=input("Please enter a sentence:")
sentence=("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus.")

letterCount = {}

for x in sentence:
    if x in letterCount:
            letterCount[x] = letterCount[x]+1
    else:
            letterCount[x]=1

keys = letterCount.keys()
for char in keys:
        print(char+":", letterCount[char])
