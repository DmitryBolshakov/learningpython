def bread(func):
    def inner():
        print("bread")
        func()
        print('bread')
    return inner

def vegetables(func):
    def inner():
        print('tomate')
        func()
        print('salad')
    return inner

def meat():
    print('ham')

sandwich = bread(vegetables(meat))
sandwich()

incorrect_sandwich = vegetables(bread(meat))
incorrect_sandwich()