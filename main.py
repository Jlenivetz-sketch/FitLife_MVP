# Приветствие пользователя
print('Приветствуем это приложение помогает следить за вашим здоровьем!')

# Узнаем данные полльзователя 
user_name = input('Введите свое имя: ')
user_age = int(input('Введите свой возраст: '))
user_weight = float(input('Введите свой вес (в килограммах): '))
user_height = float(input('Введите свой рост (в метрах): '))

# Расчет ИМТ
bmi = user_weight / (user_height ** 2)
bmi_round = round(bmi, 1)

# Расчет нормы воды в день
water_ml = user_weight * 30
water_l = water_ml / 1000

# Вывод данных для пользователя
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi_round}")
print(f"Рекомендуемая норма воды: {round(water_l, 2)} л. в день\n")
print('Расчет окончен. Будьте здоровы!')
