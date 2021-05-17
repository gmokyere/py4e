print('hello welcome to ex5')

max, min = 0.0, 0.0
setmax = True
while True:
    print("Enter a number or 'done' if finished")
    sval = input("> ")

    ## if done is entered, quit
    if sval == "done":
        break
    else:
        try:
            val = float(sval)
        except:
            print("enter something numeric duh")
            continue

    # set first number to maximum
    if setmax == True:
        max = val
        min = val
        setmax = False

    ## Find maximum
    if val > max:
        max = val

    ## Find minimum
    if val < min:
        min = val

print("max:", max, "Min:", min)
