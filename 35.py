# use constructor to copy reference the list
num1 = [10,20,30,40,50]
num2 = list(num1) # copies

num1[4] = 600
num2[1] = 200
print(num1)
print(num2)