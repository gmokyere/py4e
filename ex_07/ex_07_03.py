print("Hola welcome to ex7, pg89\n")

count = 0
tt = 0
inp = input("Please enter a filename: ")
if inp == "na na boo boo":
    print(inp.upper(), "to you too".upper())

try:
    fh = open(inp)
except:
    print("File cannot be opened or does not exist:", inp)
    quit()
for line in fh:
    line = line.strip() #delete right side white space

    #Gaurdian
    if len(line) <3:
        continue

    if not line.startswith("X-DSPAM-Confidence"): #skip lines that do not start from "from"
        continue
    word = line.split()
    count += 1
    tt += float(word[1])

print("\nThere were", count, "spam confidence with average",tt/count)
