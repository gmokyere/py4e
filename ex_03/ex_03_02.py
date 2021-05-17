hr = input("number of hours: ")
pay = input("hourly pay: ")


try:
    hrr = float(hr)
    rate = float(pay)
except:
    print("Error, please enter numeric input")
    quit()

#overtme
if hrr > 40:
    wage = rate*40
    wage+= (hrr-40)*(rate*1.5)

else:
    wage = hrr*rate
print(wage)
