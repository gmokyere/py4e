def computegrade(score):
    try:
        score = float(inp)
    except:
        print("Bad Score")
        quit()

    if score <0 or score>1:
        print("Out of range")
    elif score >= .95:
        print("A")
    elif score >= 0.8:
        print('B')
    elif score >= 0.7:
        print('C')
    elif score >= 0.6:
        print('D')
    elif score < 0.6:
        print('F')
    else:
        print("Bad score")
