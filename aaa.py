box = []
myInput = str(input()).upper()
for x in myInput:
    box.append(x)
newArray = []
for x in box:
    if x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
        newArray.append(x)
p = len(newArray)
print(p) 