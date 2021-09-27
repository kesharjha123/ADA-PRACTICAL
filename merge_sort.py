import time
import random
start = time.time()

def merge_sort(list):
    if len(list)>1:
        mid = len(list)//2 #finding middle of the list
        left_list = list[:mid] #left sublist
        right_list = list[mid:]#righ sublist
        merge_sort(left_list) #starts sorting the left
        merge_sort(right_list) #starts sorting the right
        i=0
        j=0
        k=0
        while i<len(left_list) and j<len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i=i+1
                k=k+1
            else:
                list[k] = right_list[j]
                j=j+1
                k=k+1
        while i<len(left_list):
            list[k] = left_list[i]
            i=i+1
            k=k+1

        while j < len(right_list):
            #
            list[k] = right_list[j]
            j = j + 1
            k = k + 1
    return list

my_list = list(range(1, 101))
random.shuffle(my_list)
print(my_list)
print(merge_sort(my_list))
print(my_list)
end = time.time()
runtime = (end - start)
print("Runtime: ", runtime)