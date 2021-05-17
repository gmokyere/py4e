print("holla welcome to ex6")

str = 'X-DSPAM-Confidence: 0.8475 '

ind = str.find(':')
print(ind+1)
print(float(str[ind+1:]))
