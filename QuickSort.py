import random, sys
from statistics import median
random_numbers = []
for i in range(1000):
    random_numbers.append(random.randrange(0,10000))
sys.setrecursionlimit(100000)
def quick_sort(n):
    if len(n) <= 1:
        return n
    else:
        point = n.pop(n.index(n[min(range(len(n)), key = lambda i: abs(n[i]-median(n)))]))
        #point = n.pop()
        lower_list,upper_list = [],[]
        
        for i in n:
            if i > point:
                upper_list.append(i)
            else:
                lower_list.append(i)
        return quick_sort(lower_list) + [point] + quick_sort(upper_list)
#print(quick_sort(random_numbers))