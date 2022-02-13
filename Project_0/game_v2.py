import random
import numpy as np
def random_predict(number:int=1)->int:
    """Guessing a random number with adjustment 
    Args:
        number (int, optional): Maked up number. Defaults to 1. 
    Returns:
        int: Number of tries
    """

    count = 0
    left, right = 1, 101 # Setting the initial limits of the range 

    while True:
        count += 1
        predict_number = np.random.randint(left, right) # Estimated number in range between the borders
        if predict_number == number:
            break # Exit from circle if we guessed
        elif predict_number < number:
            left = predict_number # Setting new left border 
        elif predict_number > number:
            right = predict_number # Setting new right border
    return(count)


def score_game(random_predict)->int:
    """How many attempts on average for 1000 approaches our algrithm guesses

    Args:
        random_predict ([type]): Guessing function

    Returns:
        int: Average number of attempts   
    """
    
    count_ls = [] # List for saving number of attempts
    np.random.seed(1) # Fixing seed for reproducibility
    random_array = np.random.randint(1, 101, size = (1000)) #Maked up a list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) #Finding average number of attempts
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

#RUN 
if __name__ == '__main__':
    score_game(random_predict)