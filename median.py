"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

#Sorts list
numbers = numbers.sort()

#if list has only 1 element
if len(numbers) == 1:
        print(numbers[0])
        
#list has an odd number of elements
if len(numbers) % 2 == 1 and len(numbers) > 1:
    index = len(numbers) // 2
    print(numbers[index])
else:
    #list has an even number of elements
    index = len(numbers) / 2
    median = (numbers[index] + numbers[index-1]) / 2
    print(median)





