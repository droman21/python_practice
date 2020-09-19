import random

min = 1
max = 6

while True:

    print('You Feeling Lucky? Roll The Dice!')

    answer = input()

    if answer.lower() == 'yes' or answer.lower() == 'y':

      dice_roll = random.randint(min, max)

      print(f'''

The number is ...

{dice_roll}

      ''')

    elif answer.lower() == 'no' or answer.lower() == 'n':

      print('Ok. Thank You For Playing!')

      break

    else:

      print('Come On Man. Give me a real answer...')