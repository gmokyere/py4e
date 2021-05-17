print("Hola welcome to ex10\n")

inp = input("Please enter a filename: ")

try:
    fh = open(inp)
except:
    print("File cannot be opened:", inp)
    quit()

words = fh.read() #read file to one big string
words = words.lower() #cover to lower case
tword = tuple(words) # convert to letters

# choose only alphabets
lst = list()
for w in tword:
    if w.isalpha():
        lst.append(w)

# put words in a dictionary
di = dict()
for w in lst:
    di[w] = di.get(w, 0)+1

#print in order of frequency
l = list()
for k, v in di.items():
    l.append((v,k))

newt = sorted(l, reverse = True)
print("Most frequent letters\n" )
for v, k in newt:
    print(k,v )

print("\ncongrats! Good Job on this one")
