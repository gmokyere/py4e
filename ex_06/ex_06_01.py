print("holla welcome to ex6")

text = 'X-DSPAM-Confidence: 0.8475 '

ind = text.find(':')
print(ind+1)
print(float(text[ind+1:]))
