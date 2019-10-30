w = open("betaText.txt", "r")



content = [] 
for line in w.readlines():
    content.append(line.strip())

print (content)

w.close()

