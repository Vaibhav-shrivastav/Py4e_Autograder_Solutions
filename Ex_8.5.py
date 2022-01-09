fhand = input('Enter file name: ')
if len(fhand) < 1:
    fhand = 'mbox-short.txt'
fh = open(fhand)
count = 0
for line in fh:
    x = line.rstrip().split()
    if 'From' in x:
        print(x[1])
        count+=1
    else:
        continue
print('There were', count,'lines in the file with From as the first word')
