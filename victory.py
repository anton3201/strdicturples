import random

days = {
    '03': 'первое',
    '20': 'двадцатое',
    '15': 'пятнадцотое',
    '05': 'пятое',
    '04': 'четвертое',

}

months = {
    '02': 'февраля',
    '06': 'июня',
    '09': 'сентября',
    '01': 'января',
    '04': 'апреля',
}


def convert_date(date: str) -> str:
    day, month, year = date.split('.')
    result: str = days[day] + ' ' + months[month] + ' ' + year + ' ' + 'года'
    return result


questions = {"Мэл Гибсон": '03.02.1956',
             "Джулия Ормонд": '20.06.1965',
             "Андриано Чилинтано": '15.09.1938',
             "Николас Кейдж": '05.01.1964',
             "Элвис Пресли": '04.04.1935'}

population = questions.items()

print(population)

result = dict(random.sample(population, 2))

print(result)

correctanswercount: int = 0

for question in result:
    answer = input(f"Введи год рождения актера {question}:")
    if answer == questions.get(question):
        correctanswercount = correctanswercount + 1
    else:
        print('Неправильно, правильный ответ:' + convert_date(questions.get(question)))

print(f"Правильных ответов:{correctanswercount}\n",
      f"% правильных ответов: {correctanswercount / 5 * 100}")
