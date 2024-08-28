# EX1.Create function to sum numbers in array [1,2,3,4,5,6]

def sum_array(arr):
    result = 0
    for num in arr:
        result += num
    return result


numbers = [1,2,3,4,5,6]
print(sum_array(numbers))