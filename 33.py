# copy referance the list
num1 = [10,20,30,40,50,60]
num2 = num1.copy() # copies
num2[1] = 200
num1[5] = 600
print(num1)
print(num2)