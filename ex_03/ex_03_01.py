hr = input("number of hours: ")
pay = input("hourly pay: ")
hrr = float(hr)
rate = float(pay)

#overtme
if hrr > 40:
    wage = rate*40
    wage+= (hrr-40)*(rate*1.5)

else:
    wage = hrr*rate
print(wage)
