"""
first_Name=input('What is your first name?')
Last_Name = input('What is your last name?')
full_name =(first_Name+' '+Last_Name)
print(full_name)
"""
"""
a = 1
b = int(input('What number do u prefer'))
a = type(b)
if (b == 1):
        print('It is One')
else: 
        print(a)

print('Welcome to my Calculator app')

print('What would you like to do?')
print('1. Addition')
print('2. Substract')
print('3. Multiply')
print('4. Division')
print('5. Exit')
choice = int(input('Select your choice: '))
while choice != 5:
        firstNum = float(input('Enter first number: '))
        secondNum = float(input('Enter second number: '))
        
        if choice == 1:
                print('Ans: ', firstNum+secondNum)
        elif choice == 2:
                print('Ans: ', firstNum-secondNum)
        elif choice == 3:
                print('Ans: ', firstNum*secondNum)
        elif choice == 4:
                print('Ans: ', firstNum/secondNum)
        print('What would you like to do?')
        print('1. Addition')
        print('2. Substract')
        print('3. Multiply')
        print('4. Division')
        print('5. Exit')
        choice = int(input('Select your choice: '))


def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

def hello(name='friend'):
    print (f'hello, {name}')
"""
import random
def dice():
        my_list = [1,2,3,4,5,6]
        choice = random.choice(my_list)

        print(choice)

dice()
dice()
dice()
dice()
dice()
dice()
