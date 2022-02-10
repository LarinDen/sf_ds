import numpy as np
number = np.random.randint(1,101) # set random number
count = 0

while True:
    count += 1
    predict_number = int(input("Try to guess the number from 1 to 100: "))
    
    if predict_number > number:
        print('Number must be less!')
    elif predict_number < number:
        print('Number must be more!')
    else:
        print(f'Congrats, you guessed! Right number is {number}, you made {count} tries.')
        break