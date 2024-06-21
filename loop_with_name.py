"""name = ''
while name != 'jim' :
    print ('please enter your name :')
    name = input()
print ('Thank you!')"""

'''while True:
    print('Please type your name.')
    name = input()
    if name == 'jim':
        break
print('Thank you!')'''

while True :
    print ('who are you')
    name = input()
    if name != 'jim' :
        continue    
    #the continue statement causes the program execution to jump back to the start of the loop
    print ('Hello, jimm what is your password')
    print ('Hint: it is a fish')
    password = input ()
    if password == 'goldfish' :
        break
#if the password entered is correct then it breaks out of the loop, 
#if it wrong password enetered it jumps back to the start of the loop
print ("Access Granted!")