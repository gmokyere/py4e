print("Hola welcome to ex8, pg106\n")

users = list()

count = 0
inp = input("Please enter a filename: ")
fh = open(inp)

for line in fh:
    line = line.rstrip() #delete right side white space

    #Gaurdian
    if len(line) <3:
        continue

    if not line.startswith("From "): #skip lines that do not start from "from"
        continue
    word = line.split()
    count += 1
    users.append(word[1])

print(users)
print("\nThere were", count, "words starting with 'from' ")
