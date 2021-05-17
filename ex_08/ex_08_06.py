print("Hola welcome to ex8, pg106\n")

num = list()

while True:
    inp = input("Enter a number, Enter done if done ")
    if inp == "done":
        break
    try:
        inp = float(inp)
    except:
            print("Enter a valid number")
            continue
    num.append(inp)



print("\nMax is:", max(num), "\nMin is:", min(num) )
