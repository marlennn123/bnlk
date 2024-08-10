import random
a=int(input('Томонку диапазон:'))
b=int(input('Жогорку диапазон:'))
san=0
number=random.randint(a,b)

while True:

    guess=int(input(f'{a} жана {b} ортосундагы санды табыныз:'))
    san+=1

    if guess<number:
        print('Сиз жазган сан кичине')

    elif guess>number:
        print('Сиз жазган сан чон')

    else:
        print(f'Куттуктайбыз сиз {guess} санын {san} иретте таптыныз')
        break