# EX4.Create function to find Min number in array [2,3,5,0,11,5,2]

def num(array):
    min = int(array[0])
    for i in range (len(array)):
        if array[i] < min:
            min = int(array[i])
    return min
numbers = [2,3,5,0,11,5,2]
print(num(numbers))