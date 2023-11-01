""" 1. Написати функцiю season, яка приймає один аргумент (номер
мiсяця вiд 1 до 12) та яка буде повертати пору року, якiй цей мiсяць
належить (зима, весна, лiто або осiнь). У випадку некоректного
введеного значення - виводити відповідне повідомлення
"""


def season(month_number):
    season_dict = {
        (1, 2, 12): 'Winter',
        (3, 4, 5): 'Spring',
        (6, 7, 8): 'Summer',
        (9, 10, 11): 'Autumn'
    }

    for key, value in season_dict.items():
        if month_number in key:
            return f'The season is {value}'

    return 'Incorrect month number!'


try:
    print(season(int(input("Enter month number from 1 to 12: "))))

except ValueError:
    print('Incorrect input. Enter month number from 1 to 12!')
