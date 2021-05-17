import re

print("Hello welcome to Ex11")
inp = input("please enter a file name ")
try:
    fh = open(inp)
except:
    print(inp, "cannot be opened")
    quit()


exp = input("Enter a Regular Expression of what you wanna find ")
count = 0
for line in fh:
    line = line.rstrip()
    x = re.findall(exp, line)
    if len(x) > 0:
        count += 1

print(inp, "had", count, " regular expressions that matched: ", exp)
