import random

min = 1
max = 6

while True:

    print('Do you want me to roll the dice?')

    answer = input()

    if answer.lower() == 'yes' or answer.lower() == 'y':

      dice_roll = random.randint(min, max)

      print(f'''

The number is ...

{dice_roll}

      ''')

    elif answer.lower() == 'no' or answer.lower() == 'n':

      print('Ok...')

      break

    else:

      print('Give me a real answer...')