print('hello welcome to ex5')

total = 0.0
count = 0
while True:
    sval = input("Enter a number or 'done' if finished ")

    ## if done is entered, quit
    if sval == "done":
        break
    else:
        try:
            val = float(sval)
        except:
            print("enter something numeric duh")
            continue

    count += 1
    total += val

print("total:", total, "avg:" ,total/count, "count:", count)
