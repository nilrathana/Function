# EX5.Create function to count of number 5 in array [2,3,5,0,11,5,2]

def num(array):
    count = 0
    for i in range (len(array)):
        if array[i] == 5:
            count += 1
    return count
numbers =[5,3,5,0,11,5,2]
print(num(numbers))
    