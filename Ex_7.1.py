fhand = input('Enter file name: ')
if len(fhand) < 1: fhand = 'words.txt'
fname = open(fhand)
for line in fname:
    words = line.upper().strip()
    print(words)
