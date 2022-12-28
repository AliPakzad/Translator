n = int(input())

dict1 = {}

for i in range(n):
    string = input().split()
    dict1[string[1]] = string[0]
    dict1[string[2]] = string[0]
    dict1[string[3]] = string[0]

new_string = input().split()
translatedString = []
lst = list(dict1.keys())
#print(lst)

for i in range(len(new_string)):
    if new_string[i] in lst:
        translatedString.append(dict1[new_string[i]])
    else:
        translatedString.append(new_string[i])

print(" ".join(translatedString))
