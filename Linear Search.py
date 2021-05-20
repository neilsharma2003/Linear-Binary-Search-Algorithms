'''
input integer array elements with spaces between them. Example input: 5 5 2 1 (they can be sorted or unsorted)
input target integer in array. Example input: 5
Returns index number. Example output: Element found at index 2 and 3
'''

array_elements_with_spaces = input("Insert array elements with spaces seperating:")
target = int(input("target:"))

array_elements = array_elements_with_spaces.split()
int_array = []

for i in array_elements:
    int_array.append(int(i))
int_array.sort()

for i in range(0,len(int_array)):
    if int_array[i] == target:
        print("The sorted list is now " + str(int_array) + " Element found at index " + str(i))
        
input("press ENTER to exit")
