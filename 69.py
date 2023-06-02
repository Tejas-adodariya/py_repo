# del keyword in Dictionary and clear keyword
stud1 = {
    'rno':1,
    'stud_name':"Tejas",
    'class':'BCA',
    'sem':5
}
del stud1['class']
print(stud1)

# del stud1      --> given an error when u choose this
# print(stud1)    

# clear keyword
stud1.clear()
print(stud1)