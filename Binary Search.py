
array_elements_with_spaces = input("Insert array elements with spaces seperating:")
target = int(input("target:"))

array_elements = array_elements_with_spaces.split()
int_array = []

for i in array_elements:
    int_array.append(int(i))
int_array.sort()

def binary_search(int_array, target):
    left = 0
    right = len(int_array) - 1
    while left <= right:
        mid = (left+right)// 2
        if int_array[mid] == target:
            return "Element found at index " + str(mid)
        elif int_array[mid] < target:
            left = mid + 1
        elif int_array[mid] > target:
            right = mid - 1
    return "Element not found in array"
        


    
        
