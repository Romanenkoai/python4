# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

#--------проверка на доступность модуля
f = 0
try:
    f = open ('HWork_4_4_Polynomial_Gen.py')
    from HWork_4_4_Polynomial_Gen import polynomial_gen
    from HWork_4_4_Polynomial_Gen import string_gen
    # print (type(f))
    f.close()
except FileNotFoundError:
    print ()

# имена файлов по умолчанию
file1 = 'file1.txt'
file2 = 'file2.txt'

#------- запрос на вызов модуля генирации при его доступности
if f == 0:
    print ("модуль генерации не доступен")
else:
    f = input("Будем использовать генератор? (y - да): ")
    if f == 'y':
        # file1 = input("задайте имя первого файла: ")
        polynomial_gen(file1)
        # file2 = input("задайте имя второго файла: ")
        polynomial_gen(file2)

# открываем файлы
file1 = open (file1)
file2 = open (file2)

#-------- Функция фильтрации строки из файла, для последующей обработки
def strig_filter (file_in):
    list_file = file_in.read()
    print (list_file, ' <-- строка из файла')

    simbol = False
    temp_list = ''
    for i in list_file:
        if i.isdigit():
            temp_list = temp_list + i
            simbol = False
        elif not simbol:
                temp_list = temp_list + ' '
                simbol = True

    return [int(x) for x in temp_list.split(' ')]

#------- Фильтруем строки и переворачиваем, так мне показалось удобней считать
file1_num_list = strig_filter (file1)
file1_num_list.reverse()
file2_num_list = strig_filter (file2)
file2_num_list.reverse()

#------- собственно попытка посчитать сумму
result = list(zip(file1_num_list,file2_num_list)) # да, я знаю, что zip делает выборку по наименьшей последовательности, это решить и не успел
# lenght = ((len(file1_num_list) - len(file2_num_list))**2)**0.5+len(result)

for i in range(0,len(result),2): # сумируем получившиеся после zip лщщфициенты
    result[i] = sum(result[i])

result = [result[x] for x in range(0,len(result),2)]
# for i in range(len(result)+2,lenght,2):
#     if len(file1_num_list) > len(file2_num_list):

print (file1_num_list)
print (file2_num_list)
print (result)
print ()

if not f == 0: 
    print (string_gen(result), " <-- почти результат, не хватает одночленов из длинной строки") # для того чтобы закатать обратно массив пока использован модуль, без него работать не будет

# i = list_file1[0].index('x', i)
# if isdigit (list_file1[0[i-1]])




file1.close()
file2.close()
