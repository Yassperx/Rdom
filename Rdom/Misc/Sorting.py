#Imports
import time
import matplotlib.pyplot as plt
import random

#For Evaluating the time complexity
def record(fonction, user_input):
    start = time.time()
    a = fonction(user_input)
    end = time.time()
    return (end - start) * 10000
        
#Verify if a list is sorted or not
def Check(list) -> bool:
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True
#Idk bcz it's fun
def Min(list) -> int:
    min_value : int = list[0]
    for i in list:
        if i < min_value:
            min_value = i
    return min_value
def Max(list) -> int:
    max_value : int = list[0]
    for i in list:
        if i > max_value:
            max_value = i
    return max_value
#Vrai fonctions de tris
#La nulle:
def sort_0(list):
    sorted_list = []
    while list:
        min_value = Min(list)
        list.remove(min_value)
        sorted_list.append(min_value)
    return sorted_list
#Bubble:
def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

#La meilleure:
def sort_1(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = sort_1(lst[:mid])
    right = sort_1(lst[mid:])

    return merge(left, right) 
    
#Randomizing
def Random(items : int =5, randstart : int = 1, randend : int = 30):
    randomlist = []
    for i in range(0, items):
        n = random.randint(randstart, randend)
        randomlist.append(n)
    return randomlist

