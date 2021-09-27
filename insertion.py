import time
import random
start=time.time()

def insertion_sort(list):
    for i in range (1,len(list)):
        current_value = list[i]
        position=i
        while position>0 and current_value<list[position-1]:
            list[position]=list[position-1]
            position=position-1
        list[position]=current_value
    return list


my_list = list(range(1,101))
random.shuffle(my_list)
print(my_list)
print(insertion_sort(my_list))
print(my_list)
end = time.time()
runtime = (end-start)
print("Runtime: ",runtime)


