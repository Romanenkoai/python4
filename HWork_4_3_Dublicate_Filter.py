# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def dublicate_filter (list_num = [1, 1, 2, 3, 4, 2, 1] ):

    result = list(filter(lambda x: list_num.count(x) < 2 , list_num))
    print (result)


if __name__ == '__main__':
    list_num = [int(x) for x in input("введите последовательность: ").split()]
    # +++ list_preset = [1, 1, 2, 3, 4, 2, 1] 
    # dublicate_filter ( (lambda x: x == '')(list_num))
    # ++ res = (lambda x: not x == [])(list_num)
    # print (list_num if res)
    # ++ print (list_num if res else '')
    # +++ dublicate_filter (list_num if (lambda x: not x == [])(list_num) else list_preset) 
    dublicate_filter(list_num) if (not list_num == []) else dublicate_filter()
    # fun = lambda x, y: x+y
    # ++ print (f'{(lambda x, y: x+y) (1, 2)}')
