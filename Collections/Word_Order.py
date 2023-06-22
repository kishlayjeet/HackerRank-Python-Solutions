dictionary = {}
for i in range(int(input())):
    word = input()
    if word in dictionary.keys():
        dictionary[word] += 1
    else:
        dictionary[word] = 1
print(len(dictionary))
print(*dictionary.values())