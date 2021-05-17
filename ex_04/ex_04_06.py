def computepay(hrr, rate):
    if hrr > 40:
        wage = 40*rate
        wage+= (hrr-40)*(rate*1.5)

    else:
        wage = hrr*rate
    return(wage)
