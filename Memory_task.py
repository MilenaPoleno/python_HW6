from memory_profiler import profile

"""Как видно из замеров, в первом случае
очевидной разницы нет. В случае с кратностью
общее количество выделенной памяти 
идентично, однако мы видим, что в первом 
замере изначально памяти выделяется чуть 
меньше и лишь новый список выделяет
дополнительную память"""

@profile
def my_func(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result


@profile
def my_func_new(i, j):
    result = i ** j
    return result


@profile
def multiple_num(k, l):
    num_list = [num for num in range(1, 10000)]
    new_list = []
    for el in num_list:
        if el % k == 0 or el % l == 0:
            new_list.append(el)
    return new_list


@profile
def multiple_new(m, n):
    return [num for num in range(1, 10000) if
            num % m == 0 or num % n == 0]


if __name__ == "__main__":
    my_func(1000, 10)
    my_func_new(1000, 10)
    multiple_num(15, 7)
    multiple_new(15, 7)

