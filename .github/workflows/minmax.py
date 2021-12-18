with open('test.txt') as f:
    str_num = f.readline().split()

lst_num = [int(item) for item in str_num]


def min_num(lst):
    minnum = lst[0]
    for item in lst:
        if item < minnum:
            minnum = item
    return minnum


def max_num(lst):
    maxnum = lst[0]
    for item in lst:
        if item > maxnum:
            maxnum = item
    return maxnum


def sum_num(lst):
    sumnum = 0
    for item in lst:
        sumnum += item
    return sumnum


def prod_num(lst):
    prodnum = 1
    for item in lst:
        prodnum *= item
    return prodnum

try:
    print(min_num(lst_num))
except:
    print('Overflow')

try:
    print(max_num(lst_num))
except:
    print('Overflow')

try:
    print(sum_num(lst_num))
except:
    print('Overflow')

try:
    print(prod_num(lst_num))   # у меня при переполнении возвращает inf, толкьо если в степень возвожу, то overflowerror
except:
    print('Overflow')

