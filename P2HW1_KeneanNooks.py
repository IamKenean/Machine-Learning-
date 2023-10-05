
def intinput(str):
    if len(str) > 0:
        print(str, end='')
    return int(input())

person = {
    'name':input('please enter name: '),
    'haircolor':input('please enter hair color: '),
    'hieght':input('please enter hieght in feet: '),
    'eyecolor':input('please enter eye color: '),
    'age':intinput('please enter age: '),
    'favoritefood':input('please enter favorite food: ')
}

print(f'{person["name"]} is a {person["hieght"]} tall student with {person["haircolor"]} hair and {person["eyecolor"]} eyes. They are {person["age"]} years old and their favorite food is {person["favoritefood"]}')