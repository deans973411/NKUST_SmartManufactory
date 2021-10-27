#Homework2-1
#1-Write a program input 10 numbers and determine maxima, minima, how many numbers less than 0 and how many number more than 10
print('1-Write a program input 10 numbers and determine maxima, minima, how many numbers less than 0 and how many number more than 10')

i1 = 1
NUM1 = 0
NUM2 = 0
VAL1 = list()                               #Set a list to store data
VAL1.append(input('Input number< 1>:'))     #Add first number
while i1 < 10:
    i1 += 1
    print('{}{:2}{}'.format('Input number<', i1, '>:'), end='')     #Print input information and format
    VAL0 = input()
    if VAL0 == '':                                                  #If input blank charater early stop while loop
        print('==early stop!==')
        break
    else:
        VAL1.append(VAL0)                                           #Input
VAL1 = list(map(int, VAL1))                                         #Format list data in integer   
print('The list:', VAL1)                                            #Check this list
print('Maxima:', max(VAL1))
print('Minima:', min(VAL1))
for over in VAL1:                   #Counting num>10
    if over > 10:
        NUM1 += 1
for under in VAL1:                  #Counting num<0
    if under < 0:
        NUM2 += 1
print('Num. more than 10:', NUM1)
print('Num. less than 0 :', NUM2)

#2-Write a program input 10 numbers in database, counting how many numbers are the between 30 and 1(contain)?between 60 and 10(contain)?
print('2-Write a program input 10 numbers in database')
print('counting how many numbers are the between 30 and 1(contain)?between 60 and 10(contain)?')

i2 = 1
NUM3 = 0
NUM4 = 0
VAL3 = list()                               #Set a list store values
VAL3.append(input('Input number< 1>'))      #First input
while i2 < 10:                              #A while loop for data input 10 time or early stop
    i2 += 1
    print('{}{:2}{}'.format('Input number', i2, '>'), end='')
    VAL2 = input()
    if VAL2 == '':
        print('==early stop==')
        break
    else:
        VAL3.append(VAL2)
VAL3 = list(map(int, VAL3))                 #Format the list data type
for Doman1 in VAL3:                         #Count number between 30 and 1 (contain)
    if Doman1 < 30:
        if Doman1 >= 1:
            NUM3 += 1
for Doman2 in VAL3:                         #Count number between 60 and 10 (coutain)
    if Doman2 < 60:
        if Doman2 >= 10:
            NUM4 += 1
print(VAL3)
print('Num. between 30 and 1 :', NUM3)
print('Num. between 60 and 10:', NUM4)
