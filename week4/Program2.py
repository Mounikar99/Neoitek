def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5)) 

#Function to Find Largest of Three Numbers

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print(largest(10, 25, 15))

#Program to Reverse a List
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers) 

#Program to Search for an Item in a List 

fruits = ["apple", "banana", "cherry", "grape"]
item = input("Enter fruit to search: ")

if item in fruits:
    print(f"{item} found in the list!")
else:
    print(f"{item} not found.")

 
