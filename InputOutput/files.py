"""
In this script the user enters the number of lines to write to the file.
Then the lines are written to the file, read from the file and written in revers order to another file.
"""


# The function of writing strings to a file
def write_to_file(number_of_lines=50):
    file = open('test.txt', 'w')
    for i in range(1, number_of_lines + 1):
        string = 'Test string ' + str(i) + '\n'
        file.write(string)
    file.close()


# The function of reading strings from a file and writing strings in reverse order to another file
def write_reverse():
    file = open('test.txt', 'r')
    strings_of_file = file.readlines()
    file.close()
    with open('result.txt', 'w') as result_file:  # Using construction with..as
        for i in range(1, len(strings_of_file) + 1):
            result_file.write(strings_of_file[len(strings_of_file) - i])


print('Enter the number of strings to write to the file(integer) from 2 to 1000.')
number_of_lines = input()
if number_of_lines.isdigit() == True:
    number_of_lines = int(number_of_lines)
else:
    print("You entered incorrect number or not an integer")

if 2 <= number_of_lines <= 1000:
    write_to_file(number_of_lines)
    write_reverse()
elif number_of_lines > 1000:
    print('You entered too large a number. Take pity on your computer))). We accept by default number of strings = 50')
    write_to_file()
    write_reverse()
elif number_of_lines < 2:
    print('You entered too small a number. We accept by default number of strings = 50')
    write_to_file()
    write_reverse()
