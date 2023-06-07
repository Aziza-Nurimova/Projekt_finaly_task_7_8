import numpy as np
from Projekt_0.guess_number import random_predict
from Projekt_0.Smart_guess_number import game_core_v2
from Projekt_0.metrics_of_code import score_game
def game_core_v3(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, 
    затем сужаем диапазон с обеих сторон, в зависимости от результата сравнения переменных, 
далее определяем предполагаемое число путем деления диапазона по полам, до тех пор пока не угадаем число.
    Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    left_border=1
    right_border=101
    while number!=predict:
        count+=1
        predict=left_border+(right_border-left_border)//2
        if predict > number:  right_border=predict
        elif  predict < number: left_border=predict
        else: break
        
    return count

score_game(game_core_v3)