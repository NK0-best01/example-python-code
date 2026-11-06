from collections import Counter
box = []
myInput = str(input()).upper()
words = myInput.split()
count_words = Counter(words)
print(count_words)