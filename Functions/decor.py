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

@bread
@vegetables
def meat():
    print('ham')

meat()