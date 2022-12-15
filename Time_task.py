from timeit import timeit

"""Замеры показывают, что оператор ** 
работает нaмного быстрее, чем решение 
через цикл. В примере с факториалом 
мы видим, что обычный цикл работает 
значительно медленнее цикла с генератором.
 Также в примере с делителями из замеров
 становится очевидно, что создание 
 дополнительного списка сильно увеличивает 
 время обработки"""

def my_func(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

print(timeit("my_func(5, 4)", setup=""
            "from __main__ import my_func",
            number=1000))

def my_func_new(x, y):
    result = x ** y
    return result

print(timeit("my_func_new(5, 4)", setup=""
            "from __main__ import my_func_new",
            number=1000))

def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
        yield result
# for el in fact(5):
#     print(el)

print(10000*timeit("fact(5)", setup=""
            "from __main__ import fact",
            number=3))


def fact_new(num):
    result = 1
    for el in range(1, num + 1):
        result *= el
        # print(result)

# fact_new(5)

print(10000*timeit("fact_new(5)", setup=""
            "from __main__ import fact_new",
            number=3))


def multiple_num(x, y):
    num_list = [num for num in range(1, 1000)]
    new_list = []
    for el in num_list:
        if el % x == 0 or el % y == 0:
            new_list.append(el)
    return new_list


print(timeit("multiple_num(15, 7)", setup=""
            "from __main__ import multiple_num",
            number=10))


def multiple_new(x, y):
    return [num for num in range(1, 1000) if
            num % x == 0 or num % y == 0]

print(timeit("multiple_new(15, 7)", setup=""
            "from __main__ import multiple_new",
            number=10))

