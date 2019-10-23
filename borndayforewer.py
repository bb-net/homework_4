def year():
    return input('Ввведите год рождения А.С.Пушкина:')

def day():
    return input('Ввведите день рождения А.С.Пушкина:')

question_year = year()
while question_year != '1799':
        print('Не верно')
        question_year = year()

question_day = day()
while question_day != '6':
        print('Не верно')
        question_day = day()

print('Верно')