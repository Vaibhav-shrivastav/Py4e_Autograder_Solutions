hours = int(input('no of hours: '))
rate = float(input('rate per hour: '))

if hours <= 40:
    pay = hours * rate
else:
    pay = (40 * rate) + ((hours - 40) * rate * 1.5)

print(pay)