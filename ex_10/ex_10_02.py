print("Hey there! Welcome to ex10\n")

'''Write a program to read through the mbox-short.txt and figure out the 
distribution by hour of the day for each of the messages.
 You can pull the hour out from the 'From ' lin
 '''

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
    time = words[5]      #get time of the day
    time = time.split(":")
    hour = time[0] #get on the domain name
    di[hour] = di.get(hour, 0)+1 #if word exist add one, else set default to zero and add 1


# Using tuple to find max
#Add code to the above program to figure out who has the most messages in the file.
lst = list()
for k,v in di.items():
    lst.append((k,v))

for kk,vv in sorted(lst): #note that 0:1 means print only the first element
    print(kk,vv)
