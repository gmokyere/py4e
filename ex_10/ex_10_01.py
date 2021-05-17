print("Hey there! Welcome to ex9\n")

inp = input("Please enter filename: ")
try:
    fh = open(inp)
except:
    print("file cannot be opened or does not exist: ", inp)
    quit()


di = dict()

for line in fh:
    #Gaurdian
    if len(line) < 1:
        continue

    line = line.rstrip()
    #go through each line and skip those that do start with "From "
        #NB: be sure to add space after from
    if not line.startswith("From "):
        continue
    words = line.split()  #split line into list
    email = words[1]      #get email of sender
    email = email.split("@")
    domain = email[1] #get on the domain name
    di[domain] = di.get(domain, 0)+1 #if word exist add one, else set default to zero and add 1


# Using tuple to find max
#Add code to the above program to figure out who has the most messages in the file.
lst = list()
for k,v in di.items():
    newtuple = (v,k)
    lst.append(newtuple)

lst.sort(reverse = True)

for vv, kk in lst[0:1]: #note that 0:1 means print only the first element
    print(kk,vv)
