import re

print("Hello welcome to Ex11")
inp = input("please enter a file name ")
try:
    fh = open(inp)
except:
    print(inp, "cannot be opened")
    quit()

f = fh.read()
all_nums = re.findall('[0-9]+', f)

sum = 0
for i in range(len(all_nums)):
    num = int(all_nums[i])
    sum = sum + num

print(sum)
