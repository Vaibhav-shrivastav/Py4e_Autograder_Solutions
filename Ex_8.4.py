fhand = input('Enter file name: ')
fh = open(fhand)
x = list()
for line in fh:
    word = line.rstrip().split()
    for element in word:
        if element in x:
            continue
        else:
            x.append(element)
x.sort()
print(x)