# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def number_factorization(N):
    factors = []
    divider = 2
    
    while divider <= N:
        if not N % divider:
            factors.append(divider)
            N /= divider
        else:
            divider += 1
    print ('Результат: ', factors)

if __name__ == '__main__':
    N = int(input("введите число: "))
    # print ('Результат: ', number_factorization(N))
    number_factorization(N)
