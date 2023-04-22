from timeit import timeit 
from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from QuickSort import quick_sort
from random import randrange
random_numbers = [randrange(0,1000) for i in range(1000)]

time_bubblesort = timeit(lambda: bubble_sort(random_numbers), number = 10000)
#time_insertionsort = timeit(lambda: insertion_sort(random_numbers), number = 10000)
time_quicksort = timeit(lambda: quick_sort(random_numbers), number = 10000)
#time_normalsort = timeit(lambda: random_numbers.sort(), number = 10000)
 
print(f"Bubble Sort: {time_bubblesort}")
print(f"Quick Sort: {time_quicksort}")
#print(f"Insertion Sort: {time_insertionsort}")
#print(f"Normal Sort: {time_normalsort}")
