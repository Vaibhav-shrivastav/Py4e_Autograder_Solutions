d = dict()
maximum = 0
maximum_address = ''
fhand = input('Enter File name: ')
if len(fhand) < 1 : fhand = 'mbox-short.txt'
fname = open(fhand)
for c in fname:
    word = c.split()
    if len(word) < 2 or word[0] != 'From':
        continue
    else:
        if word[1] not in d:
            d[word[1]] = 1
        else:
            d[word[1]] += 1
for address in d:
    if d[address] > maximum:
        maximum = d[address]
        maximum_address = address
print(maximum_address, maximum)