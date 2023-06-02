# Nested Dictionaries
stud1 = {
    'rno':1,
    'stud_name':"Tejas",
    'class':'BCA',
    'sem':5
}
stud2 = {
    'rno':2,
    'stud_name':"rahul",
    'class':'BCA',
    'sem':5
}
stud3 = {
    'rno':3,
    'stud_name':"milan",
    'class':'BCA',
    'sem':5
}
students = {
    'stud1' : stud1,
    'stud2' : stud2,
    'stud3' : stud3
}
print(students['stud1']['stud_name'])
print(students['stud2']['stud_name'])
print(students['stud3']['stud_name'])

# or  second type of this example



# Nested Dictionaries
# students = {
# 'stud1' : {'rno':1,'stud_name':"Tejas",'class':'BCA'},
# 'stud2' : {'rno':2,'stud_name':"rahul",'class':'BCA'},
# 'stud3' : {'rno':3,'stud_name':"milan",'class':'BCA'}
# }
# print(students['stud1']['stud_name'])
# print(students['stud2']['stud_name'])
# print(students['stud3']['stud_name'])