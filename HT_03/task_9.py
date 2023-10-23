""" 9. Користувачем вводиться початковий і кінцевий рік. 
Створити цикл, який виведе всі високосні роки в цьому 
проміжку (границі включно). P.S. Рік є високосним, якщо він кратний 4, 
але не кратний 100, а також якщо він кратний 400.
"""

start_year, stop_year = map(int, input("Enter start & stop years: ").split())

for year in range(start_year, stop_year + 1):
	if (year % 400 == 0) or ((year % 100 != 0) and (year % 4 == 0)):
		print(year)
