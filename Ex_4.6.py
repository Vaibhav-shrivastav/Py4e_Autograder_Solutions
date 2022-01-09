def computepay(h, r):
    if h<40:
        pay = h*r 
    elif h>40:
        a = h*r
        b = (h - 40.0)*(r*0.5)
        pay=a +b  
    return pay 
ab= int(input('enter hours: '))
cd= float(input('enter rate: '))
z = computepay(ab,cd)
print('Pay', z)