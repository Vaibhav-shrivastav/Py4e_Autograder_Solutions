text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
y = float(text[x+5: ])
print(y)