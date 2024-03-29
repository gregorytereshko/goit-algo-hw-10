from pulp import *

# Визначення моделі
model = LpProblem("Оптимізація_виробництва_напоїв", LpMaximize)

# Змінні рішення
x1 = LpVariable("Лимонад", lowBound=0, cat='Integer') # Кількість лимонаду
x2 = LpVariable("Фруктовий_сік", lowBound=0, cat='Integer') # Кількість фруктового соку

# Функція цілі: максимізувати загальну кількість вироблених напоїв
model += x1 + x2

# Обмеження
model += 2*x1 + 1*x2 <= 100, "Обмеження_води"
model += 1*x1 <= 50, "Обмеження_цукру"
model += 1*x1 <= 30, "Обмеження_лимонного_соку"
model += 2*x2 <= 40, "Обмеження_фруктового_пюре"

# Розв'язок задачі
model.solve()

print("Кількість лимонаду: ", x1.varValue)
print("Кількість фруктового соку: ", x2.varValue)