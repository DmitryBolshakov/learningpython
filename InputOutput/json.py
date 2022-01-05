import json
from random import choice

def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['0', '1', '2', '3', '4', '5', '6', '6', '7', '8', '9']

    while len(name) != 5:
        name += choice(letters)

    while len(tel) != 7:
        tel += choice(nums)

    person = {
        'name' : name,
        'tel' : tel
    }
    return person
def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except:
        data = []

    data.append(person_dict)
    with open('persons.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    for i in range(5):
        write_json(gen_person())



if __name__ == '__main__':
    main()

