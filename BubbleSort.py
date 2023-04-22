import random
random_numbers = []
for i in range(1000):
    random_numbers.append(random.randrange(0,10000))


def bubble_sort(numbers):
    sort = False
    while not sort:
        sort = True
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                sort = False
    return numbers 

final_list = bubble_sort(random_numbers)
#print(final_list)
