import matplotlib.pyplot as plt
import random
import numpy as np
# Данные температуры и время
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temperature = [20, 22, 23, 25, 24, 22, 21, 20, 19, 18]

# Создание линейного графика
plt.plot(time, temperature)

# Настройка осей и заголовка
plt.xlabel('Время')
plt.ylabel('Температура')
plt.title('Изменение температуры в течение дня')

# Отображение графика
plt.show()


# Список категорий товаров
categories = ['Категория 1', 'Категория 2', 'Категория 3', 'Категория 4']

# Список количества продаж
sales = [random.randint(0, 100) for _ in range(len(categories))]

# Создание столбчатой диаграммы
plt.bar(categories, sales)

# Настройка осей и заголовка
plt.xlabel('Категории товаров')
plt.ylabel('Количество продаж')
plt.title('Сравнение продаж по категориям товаров')

# Отображение диаграммы
plt.show()

# Список веса и роста
weight = [random.randint(40, 100) for _ in range(100)]
height = [random.randint(150, 200) for _ in range(100)]

# Создание точечной диаграммы
plt.scatter(weight, height)

# Настройка осей и заголовка
plt.xlabel('Вес')
plt.ylabel('Рост')
plt.title('Зависимость роста от веса')

# Отображение диаграммы
plt.show()


# Список оценок учеников
grades = [random.randint(1, 5) for _ in range(100)]

# Создание гистограммы
plt.hist(grades, bins=[1, 2, 3, 4, 5, 6])

# Настройка осей и заголовка
plt.xlabel('Оценки')
plt.ylabel('Количество учеников')
plt.title('Распределение оценок учеников по математике')

# Отображение гистограммы
plt.show()
import numpy as np

# Создание массивов x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисление значения функции z = f(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Создание двумерного графика
plt.contourf(X, Y, Z)

# Настройка осей и заголовка
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График функции z = f(x, y)')

# Отображение графика
plt.show()



# Создание массивов x и y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# Вычисление значения функции z = f(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Создание двумерного графика
plt.contourf(X, Y, Z)

# Настройка осей и заголовка
plt.xlabel('X')
plt.ylabel('Y')
plt.title('График функции z = f(x, y)')

# Отображение графика
plt.show()