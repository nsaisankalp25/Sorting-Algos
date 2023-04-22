"""import random
random_numbers = [68, 4, 71, 72, 97, 26, 95, 32, 67, 98]
for i in range(10):
    random_numbers.append(random.randrange(0,100))

def insertion_sort(unsorted_list:list) -> list:
    length = range(1, len(unsorted_list))
    for i in length:
        current_value = unsorted_list[i]
        print(current_value)
        while current_value < unsorted_list[i-1] and i > 0:
            unsorted_list[i-1], unsorted_list[i] = unsorted_list[i], unsorted_list[i-1]
            i -= 1
    return unsorted_list
insertion_sort([1,3,2,5,4,7])"""




def ins_sort(nums):
    for i in range(1,len(nums)):
        current_value = nums[i]
        while current_value < nums[i-1] and i > 0:
            nums[i-1], nums[i]  =nums[i], nums[i-1]
            i = i - 1
    print(nums)
    
ins_sort([0,1,9,7,9,4,5,7,8,4,7])

