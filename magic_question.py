import random
import time

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как вас зовут?')
name = input()
print(f'Привет, {name}!')

def information():
    print('Сколько вам полных лет?')
    age = int(input())
    print('Какого вы пола? (М = муж., Ж = жен.)')
    gender = input().lower()
    if gender == 'м':
        gender = 'парень'
    elif gender == 'ж':
        gender = 'девушка'

    print('У вас есть вторая половинка? (Д = да, Н = нет)')
    love = input()
    if love.lower() == 'д':
        love = 'есть вторая половинка'
    elif love.lower() == 'н':
        love = 'нет второй половинки'
    print(f'Вам {age} лет, вы {gender} и у вас {love}')
information()

print()
while True:
    print('Задайте ваш вопрос и я на него отвечу!')
    print('Воспрос должен быть таким чтобы я отвечал только ДА и НЕТ')

    question = input()
    def sleep():
        print('Связываюсь с вселенной...')
        time.sleep(1)
        print('Ловлю контакт...')
        time.sleep(1)
        print('И...')
        time.sleep(1)
    sleep()
    bay = 'До новых встреч'
    answer = random.choice(answers)
    print(answer)

    print('Вы хотите задать еще вопрос? (Д = да, Н = нет)')
    never = input()
    if never.lower() == 'н':
        print(bay)
        break