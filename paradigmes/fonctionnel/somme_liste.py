import functools

my_list = [1, 2, 3, 4, 5]


def add_it(x, y):
    return (x + y)


sum = functools.reduce(add_it, my_list)
print(sum)

sum = functools.reduce(lambda x, y: x + y, my_list)
print(sum)


# square = lambda x: x**2
# double = lambda x: x + x


def square(x): return x**2


def double(x): return x + x


print(list(map(square, my_list)))
print(list(map(double, my_list)))

my_list = [1, 2, 3, 4, 5]
sum = functools.reduce(lambda x, y: x + y, my_list)
print(sum)
