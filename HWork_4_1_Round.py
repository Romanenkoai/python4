# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


import math


round_value = int(input("введите число (кол-во знаков после запятой): "))
# -----------
# round_value = 4
num = str(math.pi)
dot_index = num.index('.')

# for round_value in range(1, 11):
round_index = dot_index + round_value

if num[round_index+1] >= '5':
    num = str(float(num)+10**-round_value)

print(float(num[:round_index+1]))
# -------------
print ('\nили')
# round_value = 7
num = math.pi
num = num + (num % (10**-round_value)) # тут определяется правило округления
num = num * (10**round_value) # перемещаем точку
num = num//1 # отезаем дробную часть
num = num / 10**round_value # возвращаем точку
print(num)
# ------------

print ('\nпроверка round')
print(round(math.pi,round_value))
