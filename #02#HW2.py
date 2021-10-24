#Class: MDE4-3 Name: Dean Lin
print("Class: MDE4-3 Name: Dean Lin")

#1-Run the Prograam count from 1 to 100, show the odd number between 21 and 50 and calculate their summation.
print("1-Run the Program count from 1 to 100, show the odd number between 21 to 50 and calculate their summation.")   

i1 = 0                                  #Defind data type in integer, reset counting loop
SUM1 = 0                                #Defind data type in integer, summation data from 0 
for i1 in range(1, 100, 1):             #Count from 1 to 100: Range(initial, final, count by)
    if i1 >= 21 and i1 <= 50:           #Defind the Range which form 21 to 50
        if i1 % 2 == 1:                 #Defind odd number
            print(i1," ", end='')
            SUM1 += i1                  #Calculate the summation
print('\nThe odd number summation between 21 to 50 is:', SUM1)
print('\n')


#2-Multiplication Table (9x9) arrange in order
print("2-Multiplication Table (9x9) arrange in order")

NUM1 = 1
while NUM1 < 10:                        #Defind the Multiplication table final number in 9
    NUM1 += 1                           #Defind the Multiplication tbale initial number in 2
    for y in range(NUM1-1, NUM1):
        for x in range(2, 10):
            print('{}x{}={:2} '.format(x, y, x*y), end='')      #Setup Table format
    print('\n\n')


#3-Type in 10 students' scores, print tiptop score, minima score and reject number
print("3-type in 10 students' score, print tiptop score, minima core and reject number")
print("***Remind, the maxima type in data be set less than 10 times***")

i2 = 1
NUM2 = 0
CLASS_SCORE = list()                                            #Set a list which store input data
CLASS_SCORE.append(input("Please ttype in Score< 1 >\n"))       #First type in massage
while True:
    i2 += 1                                                     #Counter for type in time
    if i2 > 10:                                                 #Stop the input program when input data count to 10
        print("You type in 10 Score")
        break
    print("Please type in Score<", i2, ">")                     #Type in message when after first time
    Std_SCORE = input()
#    Std_SCORE = int(Std_SCORE)
#    if Std_SCORE >= 100 or Std_SCORE <= 0:
#        print("You type in Failed Score，the program stoping(SCORE>100, SCORE<0)")
#        break
    if Std_SCORE == "":                                         #Early stop when detect a blank charater
        print("You type in blank charater, early stop")
        print("you type in", i2-1,"data")
        break
    else:
        CLASS_SCORE.append(Std_SCORE)
CLASS_SCORE = list(map(int, CLASS_SCORE))                       #List all classmate's score
for Failed_SCORE in CLASS_SCORE:
    Failed_SCORE = int(Failed_SCORE)
    if Failed_SCORE < 60:                                       #Check the score less than minimum passing mark
        NUM2 += 1                                               #Counter
  
print('The class score data:', CLASS_SCORE)
print("The tiptop score in class:", max(CLASS_SCORE), " the minima score in class:", min(CLASS_SCORE))
print("Reject number in class", NUM2)
print("\n\n")


#4-Type in electricity, calculate amount payable.(Taiwan Powar cop. less than 100kWh: 2.2NTW/kWh, 101kWh to 300 kWh: 3.3NTW/kWh, Exceed 300 kWh: 4.4NTW/kWh)
print("4-Type in electricity, calculate amount payable.(Taiwan Powar cop. less than 100kWh: 2.2NTW/kWh, 101kWh to 300 kWh: 3.3NTW/kWh, Exceed 300 kWh: 4.4NTW/kWh)")

[EM1, PR1] = [0, 2.2]   #EM1 definded as a integer was rank 1
[EM2, PR2] = [0, 3.3]   #EM2 definded as a integer was rank 2
[EM3, PR3] = [0, 4.4]   #EM3 definded as a integer wes rank 3
NUM3 = input('Please type in Electricity:')
NUM3 = int(NUM3)        #Defind NUM3 be integer and electricity data

if NUM3 <= 100:                         #Calculate amount payable when electricity less than 100 kWh
    SUM2 = NUM3 * PR1
if NUM3 > 100 and NUM3 <= 300:          #Calculate amount payable when electricity between  101 kWh to 300 kWh
    SUM2 = 100 * PR1 + (NUM3 - 100) * PR2
if NUM3 > 300:                          #Calculate amount payable when electricity exceed 300 kWh 
    SUM2 = 100 * PR1 + 200 * PR2 + (NUM3 - 300) * PR3
print("Summation your electricity:", SUM2, "NTW")
print('\n\n')


#5-Build a correspond right triangel and a correspond equilateral triangel refer to input value
print("1-Build a correspond right triangel and a corresond equilateral triangel refer to input value\n")

#5-1 Make a right triangel
NUM4 = input('5-1 Type in a number to make a correspond right triangel:')
NUM4 = int(NUM4)

VAL0 = 0
while VAL0 < NUM4:
    VAL0 += 1
    print(VAL0 * "X")                   #Place correspond charater make a triangel shape

#5-2 Make a equilateral triangel
NUM5 = input('5-2 Type in a number to make a correspon equilateral triangel:')
NUM5 = int(NUM5)

VAL1 = 0
while VAL1 < NUM5:
    VAL1 += 1
    print((NUM5 - VAL1) * ' '+(1 + 2 *(VAL1 - 1)) * "X")    #Make the triangel align center which place correspond blank charater 
print('\n')
