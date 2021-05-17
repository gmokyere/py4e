print("Hola welcome to ex8, pg105\n")

fh = open('romeo.txt')
words = list() #create empty list

for line in fh:
    wrd = line.rstrip()
    wrd = wrd.split() ##split lines into list
    for word in wrd:
        if word not in words: ## append all unique words
            words.append(word)

print(sorted(words))
