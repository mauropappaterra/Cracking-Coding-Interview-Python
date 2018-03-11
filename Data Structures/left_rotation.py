# Cracking the Coding Interview
# left_rotation.py
# Created by Mauro J. Pappaterra on 11 of March 2018.

def array_left_rotation(array, size, shifts):
    #print(array)
    shifts = shifts % size # wraps around after size is exceeded

    new_array = [None] * size

    for index, element in enumerate(array):
        new_index = (index - shifts) + (size + 1) % (size + 1)
        new_array[new_index] = element

    #print (new_array)
    string = ''

    for number in new_array:
        string += str(number) + ''

    return string

# FOR HACKER RANK EXTERNAL INPUT
#n, k = map(int, input().strip().split(' '))
#a = list(map(int, input().strip().split(' ')))
#answer = array_left_rotation(a, n, k);
#print(*answer, sep=' ')

# FOR TESTING PURPOSES
print(array_left_rotation([1, 2, 3, 4, 5],5,4))
print(array_left_rotation([1, 2, 3, 4, 5],5,12))
print(array_left_rotation([1, 2, 3, 4, 5],5,-2))
print(array_left_rotation([1, 2, 3, 4, 5, 6, 7, 8, 9],9,4))
