# Ascending Order
def bubbleSortAscending(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] > list[j + 1]:
                temp_element = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp_element


# Descending Order
def bubbleSortDescending(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(i):
            if list[j] < list[j + 1]:
                temp_element = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp_element


num_list = [3, 9, 3, 5, 2, 6, 8, 7, 1]

bubbleSortDescending(num_list)
print(num_list)
