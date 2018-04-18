def reverse_string(thingToReverse):
    return thingToReverse[::-1]

def partition(thing):
    stuff = ['a','b','c','d','e','g','h','i','j','k','l','m']
    return [things for things in thing if things[0].lower() in stuff]

def labMenu():
    print('Enter 1 for Problem 3.32')
    print('Enter 2 for Problem 3.33')
    print('Enter 3 for Problem 3.40')
    print('Enter 4 to exit the program')

while True:
    labMenu()
    choice = int(input('Please make an entry: '))

    if choice == 1:
        value = int(input('Enter value: '))
        firstDigit = value % 10
        secondDigit = (value % 100)//10
        thirdDigit = (value % 1000)//100
        fourthDigit = (value % 10000)//1000
        print(fourthDigit)
        print(thirdDigit)
        print(secondDigit)
        print(firstDigit)
        break
    elif choice == 2:
        origString = input('Enter string to be reversed: ')
        x = reverse_string(origString)
        print(x)
        break
    elif choice == 3:
        nameList = eval(input('Enter the list of names: '))
        x = partition(nameList)
        for i in x:
            print(i)
        break
    elif choice == 4:
        break
    
