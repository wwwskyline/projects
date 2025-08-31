import random

print('Привет!Давайте поиграем в числовую угадайку?')
print('Давайте введем границы нашей Угадайки.')


def game():
    a = True
    while a:
        limit1 = input('Введите начальное число: ')
        limit2 = input('Введите конечное число: ')
        if limit1.isdigit() and limit2.isdigit():
            limit1 = int(limit1)
            limit2 = int(limit2)
            num = random.randint(limit1, limit2)
            print('Отлично! Теперь приступим к игре.')

            n = 0
            count = 0
            while n != num:
                n = input(f'Введите число от {limit1} до {limit2}: ')
                if n.isdigit():
                    n = int(n)
                else:
                    print('Введите число в допустимых границах!')
                    continue

                if n > limit2 or n < limit1:
                    print('Введите число в допустимых границах!')
                    continue

                if n > num:
                    print('Ваше число больше загаданного!Попробуйте ещё раз.')
                    count += 1
                    continue
                if n < num:
                    print('Ваше число меньше загаданного!Попробуйте ещё раз.')
                    count += 1
                    continue
            if n == num:
                count += 1
                print('Поздравляем!Вы угадали!')
                print('Число попыток: ', count)
                while a:
                    b = input('Сыграем ещё раз? Д - да, Н - нет :) : ')
                    if b.lower() == 'д':
                        a = True
                        game()
                    if b.lower() == 'н':
                        a = False
                        break
                    else:
                        print(
                            'Введите "Д", если хотите продолжить игру. \nВведите "Н", если хотите закончить!')               
                        continue
        else:
            print('Можно вводить только цифры от 1 до ...')
            continue


game()
print('До встречи!')