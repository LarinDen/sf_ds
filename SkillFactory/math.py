x = 8  #6.5
y = 22 #7.2
z = 15 #11.4
for a in range(-5, 5, 1):
    for b in range(-5, 5, 1):
        for c in range(-5, 5, 1):
            if a*x + b*y + c*z == 20: #3.8:
                print(f'a = {a}, b = {b}, c = {c}')
                #print(f'total = {a*33 + b*17 + c*47}')
                print(f'total = {a*17 + b*45 + c*31}')