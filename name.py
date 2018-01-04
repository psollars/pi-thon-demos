name = input('What is your name?')

print('Hello, ' + name)

age = int(input('How old are you?'))

print('I know that your name is ' + name + ' and you\'re '+ str(age) + ' years old.')

if age >= 16 :
    print(name + ' is old enough to drive')
else :
    print('sorry, ' + name + ' isn\'t old enough to drive')
