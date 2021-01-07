x = [ [5,2,3], [10,8,9] ] 

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

z = [ {'x': 10, 'y': 20} ]

def iterateDictionary(students):
    for student in students:
        keys = [k for k in student.keys()]
        temp = keys[0] + " - " + student[keys[0]] + " , " + keys[1] + " - " + student[keys[1]]
        print(temp)
    return 0
        
def printDojoInfo(dojo):
    for k in dojo.keys():
        print(str(len(dojo[k])) + " " + k.title())
        for i in dojo[k]:
            print(i)
        print("")
    return 0

print('==Part 1==')
x[1][0] = 15
students[0]['last_name'] = 'Bryant'
z[0]['y'] = 30

print('==Part 2==')
iterateDictionary(students)

print('==Part 3==')
printDojoInfo(dojo)