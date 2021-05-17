import re

print("Hello welcome to Ex11")
inp = input("please enter a file name ")
try:
    fh = open(inp)
except:
    print(inp, "cannot be opened")
    quit()


#Find all lines of the form, "New Revision: 39772" and compute the average
total = 0.
count = 0
for line in fh:
    line = line.rstrip()
    x = re.findall("^New Revision: ([0-9]+)", line)
    for n in x:
        if len(n) > 0:
            count += 1
            total += float(n)

print("Average is:" ,int(total/count))
