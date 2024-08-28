# EX7.Create function to count negative number in array [-1,11,2,0,-1,4]

def num(array):
    count_negative = 0
    for i in range (len(array)):
        if array[i] < 0:
            count_negative += 1

    return count_negative
numbers = [-1,11,2,0,-1,4]
print(num(numbers))