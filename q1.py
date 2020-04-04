setOne = [[1,3,5,7],[9,11,13,15],[17,19,21,23],[26,27,30,31]]
setTwo = [[2,3,6,7],[10,11,14,15],[18,19,22,23],[26,27,30,31]]
setThree= [[4,5,6,7],[12,13,14,15],[20,21,22,23],[28,29,30,31]]
setFour = [[8,9,10,11],[12,13,14,15],[24,25,26,27],[28,29,30,31]]
setFive=[[16,17,18,19],[20,21,22,23],[24,25,26,27],[28,29,30,31]]

birthday = 0     #Add the first number of each set to this

print('Question #1: Is your birthday in Set 1?\n')
for x in setOne:        #Pretty Prints the Matrix
    print(*x, sep=" ") 
print('\n')
answerSetOne = input('Enter (n)o or (y)es: ')
if ( answerSetOne == 'y'):
    birthday += setOne[0][0]
     
print('Question #2: Is your birthday in Set 2?\n')
for x in setTwo:        #Pretty Prints the Matrix
    print(*x, sep=" ")
print('\n')
answerSetTwo = input('Enter (n)o or (y)es: ')
if ( answerSetTwo == 'y'):
    birthday += setTwo[0][0]
    
print('Question #3: Is your birthday in Set 3?\n')
for x in setThree:      #Pretty Prints the Matrix
    print(*x, sep=" ")
print('\n')
answerSetThree = input('Enter (n)o or (y)es: ')
if ( answerSetThree == 'y'):
    birthday += setThree[0][0]

print('Question #4: Is your birthday in Set 4?\n')
for x in setFour:       #Pretty Prints the Matrix
    print(*x, sep=" ")
print('\n')
answerSetFour = input('Enter (n)o or (y)es: ')
if ( answerSetFour == 'y'):
    birthday += setFour[0][0]

print('Question #5: Is your birthday in Set 5?\n')
for x in setFive:       #Pretty Prints the Matrix
    print(*x, sep=" ")
print('\n')
answerSetFive = input('Enter (n)o or (y)es: ')
if ( answerSetOne == 'y'):
    birthday+= setFive[0][0]
    
print('Your birthday is '+str(birthday)+'!')