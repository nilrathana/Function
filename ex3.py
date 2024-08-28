# EX3.Create function to find Max number in array [2,3,5,0,11,5,2]

def num(arr):
    max = int(arr[0])
    for i in range (len(arr)):
        if arr[i] > max:
            max = int(arr[i])
    return max
numbers = [2,3,5,0,11,5,2]
print(num(numbers))