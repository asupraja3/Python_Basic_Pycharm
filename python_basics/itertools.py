from itertools import *

# count itertools
def count_example():
    counter = count(start=5, step=2)
    for _ in range(5):
        print(next(counter))
count_example()
# cycle itertools
def cycle_example():
    cycled = cycle(['A', 'B', 'C'])
    for _ in range(6):
        print(next(cycled))
cycle_example()

# Common itertools
def common_example():
    data = [1, 2, 3, 4, 5]
    repeated = repeat(data, times=2)
    for item in repeated:
        print(item)
common_example()

# accumulate itertools
def accumulate_example():
    data = [1, 2, 3, 4, 5]
    accumulated = accumulate(data)
    for item in accumulated:
        print(item)
accumulate_example()

# chain itertools
def chain_example():
    data1 = [1, 2, 3]
    data2 = ['A', 'B', 'C']
    chained = chain(data1, data2)
    for item in chained:
        print(item)
chain_example()

# product itertools
def product_example():
    data1 = [1, 2]
    data2 = ['A', 'B']
    producted = product(data1, data2)
    for item in producted:
        print(item)
product_example()

