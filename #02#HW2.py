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
CLASS_SCORE = list()
CLASS_SCORE.append(input("Please ttype in Score< 1 >\n"))
while True:
    i2 += 1
    if i2 > 10:
        print("You type in 10 Score")
        break
    print("Please type in Score<", i2, ">")
    Std_SCORE = input()
#    Std_SCORE = int(Std_SCORE)
#    if Std_SCORE >= 100 or Std_SCORE <= 0:
#        print("You type in Failed Score，the program stoping(SCORE>100, SCORE<0)")
#        break
    if Std_SCORE == "":
        print("You type in blank cell, early stop")
        print("you type in", i2-1,"data")
        break
    else:
        CLASS_SCORE.append(Std_SCORE)
CLASS_SCORE = list(map(int, CLASS_SCORE))
for Failed_SCORE in CLASS_SCORE:
    Failed_SCORE = int(Failed_SCORE)
    if Failed_SCORE < 60:
        NUM2 += 1
  
print('The class score data:', CLASS_SCORE)
print("The tiptop score in class:", max(CLASS_SCORE), " the minima score in class:", min(CLASS_SCORE))
print("Reject number in class", NUM2)
print("\n\n")


#4輸入用電度數，計算應繳電費(台電100度以下2.2元/度，101~300 3.3元/度，300度以上4.4元)
print("4-輸入用電度數，計算應繳電費(台電100度以下2.2元/度，101~300 3.3元/度，300度以上4.4元)")

[EM1, PR1] = [0, 2.2]   #定義EM1為第一區間整數，PR1為第一區間計價
[EM2, PR2] = [0, 3.3]   #定義EM2為第一區間整數，PR2為第二區間計價
[EM3, PR3] = [0, 4.4]   #定義EM3為第一區間整數，PR3為第三區間計價
NUM3 = input('請輸入度數:')
NUM3 = int(NUM3)

if NUM3 <= 100:
    SUM2 = NUM3 * PR1
if NUM3 > 100 and NUM3 <= 300:
    SUM2 = 100 * PR1 + (NUM3 - 100) * PR2
if NUM3 > 300:
    SUM2 = 100 * PR1 + 200 * PR2 + (NUM3 - 300) * PR3
print("累進計算出您的電費為:", SUM2, "元")
print('\n\n')


#5輸入一數字印出相對應層數的直角三角形與金字塔
print("1-輸入一數字印出相對應層數的直角三角形與金字塔\n")

#5-1 製作直角三角形
NUM4 = input('5-1 輸入數字以製作直角三角形:')
NUM4 = int(NUM4)

VAL0 = 0
while VAL0 < NUM4:
    VAL0 += 1
    print(VAL0 * "X")

#5-2 製作金字塔
NUM5 = input('5-2 輸入數字以製作金字塔:')
NUM5 = int(NUM5)

VAL1 = 0
while VAL1 < NUM5:
    VAL1 += 1
    print((NUM5 - VAL1) * ' '+(1 + 2 *(VAL1 - 1)) * "X")
print('\n')
