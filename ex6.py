# EX6.Create function to count positive number in array [-1,11,2,0,-1,4]

def num(array):
    count_positive = 0
    for i in range (len(array)):
        if array[i] >= 0:
            count_positive += 1

    return count_positive
numbers = [-1,11,2,0,-1,4]
print(num(numbers))
    
