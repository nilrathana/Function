# EX2.Create function to sum odd number in array [1,2,3,4,5,6]

def sum(odd_number):
    total = 0
    for i in range (len(odd_number)):
        if int(odd_number[i])%2==1:
            total += int(odd_number[i])
    return total

numbers = [1,2,3,4,5,6]
print(sum(numbers))