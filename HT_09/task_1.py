""" 1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів. Після 
   запуска програми на екран виводиться в лівій половині - колір 
   автомобільного, а в правій - пішохідного світлофора. Кожну 1 секунду
   виводиться поточні кольори. Через декілька ітерацій - відбувається
   зміна кольорів - логіка така сама як і в звичайних світлофорах
   (пішоходам зелений тільки коли автомобілям червоний).

   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Red
      Yellow     Red
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""


from time import sleep


def color_for_pedestrian(car_light):

    pedestrian_color_dict = {
        'Red': 'Green',
        'Yellow': 'Red',
        'Green': 'Red'
    }

    return pedestrian_color_dict[car_light]


def color_for_car(cycle_iteration):

    car_color_dict = {
        (0, 1, 2, 3): 'Red',
        (4, 5, 10, 11): 'Yellow',
        (6, 7, 8, 9): 'Green'
    }

    for key, value in car_color_dict.items():
        if cycle_iteration in key:

            return value


def traffic_light_cycle(total_seconds_of_iterations):

    for iteration in range(total_seconds_of_iterations):
        cycle_iteration = iteration % 12

        car_light = color_for_car(cycle_iteration)
        pedestrian_light = color_for_pedestrian(car_light)

        print(car_light, pedestrian_light.rjust(15 - len(car_light)))
        sleep(1)


time_of_execution = int(input("Enter time of execution in seconds: "))
traffic_light_cycle(time_of_execution)
