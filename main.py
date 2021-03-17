from getGPAscale import gpaScale
from classes import classes
from calculateGPA import calcGPA
import json

print('Please enter your full name: (This program only holds one user/scale at a time)')
name = input()

#import GPA scale
print('Do you want to import a new GPA scale? Respond y or n')
if input() == 'n':
  pass
else:
    person = gpaScale(name)
    with open('unweightedscale.json', 'r') as f:
        scale = json.load(f)
        for key in person.scale:
            scale[key] = {}
            scale[key] = person.scale[key]
    with open('unweightedscale.json', 'w') as f:
        json.dump(scale, f)
    with open('weightedscale.json', 'r') as f:
        scale = json.load(f)
        for key in person.weighted_scale:
            scale[key] = {}
            scale[key] = person.weighted_scale[key]
    with open('weightedscale.json', 'w') as f:
        json.dump(scale, f)


#import classes
print('Do you want to import new classes and grades? Respond y or n')
if input() == 'y':
    with open('grades.json', 'w') as f:
        json.dump({}, f)
    with open('credits.json', 'w') as f:
        json.dump({}, f)
    with open('level.json', 'w') as f:
        json.dump({}, f)
    print('Your classes/grades have been cleared')
    person = classes(name)
    with open('grades.json', 'r') as f:
        grades = json.load(f)
        for key in person.grades:
            grades[key] = {}
            grades[key] = person.grades[key]
    with open('grades.json', 'w') as f:
        json.dump(grades, f)
    with open('credits.json', 'r') as f:
        info = json.load(f)
        for key in person.credits:
            info[key] = {}
            info[key] = person.credits[key]
    with open('credits.json', 'w') as f:
        json.dump(info, f)
    with open('level.json', 'r') as f:
        info = json.load(f)
        for key in person.level:
            info[key] = {}
            if person.level[key] == 1:
                temp = 'AP'
            elif person.level[key] == 2:
                temp = 'Honors'
            else:
                temp = 'CP'
            info[key] = temp
    with open('level.json', 'w') as f:
        json.dump(info, f)


with open('level.json', 'r') as a:
    lvls = json.load(a)
    with open('grades.json', 'r') as b:
        grds = json.load(b)

        grades = ''

        person = calcGPA(name)
        print("\n\n_______________________________________")
        print(f'{name}\'s Classes and Grades are:')
        for key in lvls:
            print(lvls[key] + ' ' + key + ': ' + grds[key])
        print("_______________________________________")
        print(f'{name}\'s Unweighted GPA is ' + str(round(person.unweighted_gpa, 2)))
        print("_______________________________________")
        print(f'{name}\'s Weighted GPA is ' + str(round(person.weighted_gpa, 2)))
        print("_______________________________________")









