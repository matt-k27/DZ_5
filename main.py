print('DZ5')

originalList = [1, 2, 3, 4, 5]
result = []

if originalList:
    separator = int(len(originalList) / 2)
    if len(originalList) % 2:
        result = [originalList[:separator+1], originalList[separator+1:]]
    else:
        result = [originalList[:separator], originalList[separator:]]
else:
    result = [[], []]


print(result)

print('Thank you for using')