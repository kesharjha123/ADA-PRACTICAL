import time
import random
start = time.time()

def bubble_sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
    print(list)


my_list = list(range(100))
random.shuffle(my_list)
print(my_list)
bubble_sort(my_list)

end = time.time()
runtime = (end-start)
print("Runtime: ",runtime)