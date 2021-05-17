print('hello welcome to ex7')
inp = input("Enter a file you would like to read:")
try:
    fh = open(inp) #create file handle
except:
    print("Error in filename")
    quit()

for line in fh:
    ly = line.rstrip() #delete right space
    print(ly.upper()) #convert to upper
print("\ncongrats file read successfully...".upper())
