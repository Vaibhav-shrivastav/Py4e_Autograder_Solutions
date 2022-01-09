fname = input("Enter file name: ")
fh = open(fname)
count = 0
y = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        pos = line.find(" ")
        num = float(line[pos+1:])
        y = y + num

print('Average spam confidence:', y/count)