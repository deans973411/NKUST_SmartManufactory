#HW3
#Class:MDE4-3 Name:Dean Lin
print('HW3')
print('Class:MDE4-3 Name:Dean Lin')

#1-0 Key in classmate score using 'list'
print("1-0 Key in classate score using 'list'")
print('tip:Formate{Score1}{blank}{Score2}{blank}{Score3}')
Ch = list()
En = list()
Ma = list()
i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0
NUM1 = 0
NUM2 = 0
NUM3 = 0
VAL1 = 0
while True:
    IN1 = input('Chinese/English/Mathmatic>')                       #Get the input data
    NUM1 = IN1.count(' ')                                           #Classification the blank character for check it format
    if NUM1 == 2:                                                   #Check Gate1--2 blank : accept!
        try:                                                            #format string 2 blank to 3 word
            Chi, Eni, Mai = map(int, IN1.split())
        except:
            print('=Type in score number ERROR=')                       #Check Gate2--format not 0_0_0 : Fail!(re type)
            continue
        if Chi > 100 or Eni > 100 or Mai > 100:                         #Check Gate2--Score over than 100 : Fail!(re type)
            print('=Type in score over than 100=')
            continue
        elif Chi < 0 or Eni < 0 or Mai < 0:                             #Check Gate2--Score less than 0   : Fail!(re type)
            print('=Type in score less than 0=')
            continue
        else:
            i1 += 1                                                             #type in counter
            Ch.append(Chi)                                                      #Put data 'Chi' in Ch list
            En.append(Eni)                                                      #Put data 'Eni' in En list
            Ma.append(Mai)                                                      #Put data 'Mai' in Ma list
            #print(Ch)
            #print(En)
            #print(Ma)
    elif NUM1 == 1 or NUM1 > 2:                                     #Check Gate1--a balck or more then 2 blank : Fail!(re type)
        print('==Format error or type in fail, please try again==')
        continue
    else:                                                           #Check Gate1--nothing INPUT : ending type in program, continue
        print('Total type in ', i1,'datas')
        break
print('Total output ', i1, 'dates')

#1-a Search how many people all of their 3 subject score more than 90.
print('1-a Search how many people all of their 3 subject score more than 90')
'''
The OLD version>>
    if i2 <= i1:                                    #If loop to count how many
        a1 = Ch[i2]
        b1 = En[i2]
        c1 = Ma[i2]
        if a1 >= 90 and b1 >= 90 and c1 >= 90:
            NUM2 += 1
        i2 += 1                                     #counter
<<
In the loop, if you use 'if loop' with counter，the program will present you-
    IndexError: list index out of range
It difficult to fix it now(maybe can in future), just try to use now version.
It'll be fixed when this loop format change to 'For loop'
'''
while True:
    for i2 in range(0, i1, 1):                              #Put the data form 0 ~ last one to a1, b1 and c1
        a1 = Ch[i2]                                 ###You just can input value using 'For loop', you have no choise
        b1 = En[i2]
        c1 = Ma[i2]
        if a1 >= 90 and b1 >= 90 and c1 >= 90:              #Using 'And Gate' to check a1 to c1
            NUM2 += 1                                       #If currect, counter plus one
    else:
        print("All of 3 subjects score over 90 are", NUM2, "people")    #Out put the result
        break


#1-b Chinese highest score in the class
print('1-b Chinese highest score in the class')
try:
    print('Chinese highest score in the class got:', max(Ch))           #Claculate Maxima in Chinese database: Ch() list
except ValueError:                                                      #If no data lead to ValueError, Pass 
    print('No data')
    pass


#1-c Mathmatic highest score in the class
print('1-c Mathmatic highest score in the class')
try:
    print('Mathmatic highest score in class is:', max(Ma))              #Calculate Maxima in Mathmatic data base: Ma() list
except ValueError:                                                      #If no data lead to ValueError, pass
    print('No data')
    pass


#1-d How many people are they English fail?
print('1-d How many people are they English fail')
for i3 in range(0, i1, 1):                                              #Extract data form English database: En() list
    c2 = En[i3]
    if c2 < 60:                                                         #Set the Fail score less than 60, if true counter plus 1
        NUM3 += 1
print('Total English fail people are:', NUM3)                           #Print the result


#1-e All subject average score?
print('1-e All sbject average score')
for i4 in range(0, i1, 1):                                              #Extract data form database, add all score and calculate average score
    a3 = int(Ch[i4])
    b3 = int(En[i4])
    c3 = int(Ma[i4])
    VAL1 += (a3 + b3 + c3)
 
print('Average of all subject in this class:', (VAL1 / i1 / 3))         #Print the calculated result


#1-f(own) Search someone's score
print("1-f(own) Search the student's score")

print('Classmate No.:', end='')
for i5 in range(1, i1+1, 1):                                            ##Options###
    print('{:2}, '.format(i5), end='')                                  #Show all the score in order
print("\nChinese Score", Ch)
print("English Score", En)
print("Mathmatic Score", Ma)
search = int(input('Search the student ID number:'))                    #Input a number who you want search
search = search - 1                                                     #translate input number to datebase serial number
a = Ch[search]                                                          #print value to a, b, c
b = En[search]
c = Ma[search]
print("\nNo.", search + 1, "person score is:\n", "Chinese:", a, "English:", b, "Mathmatic:", c)     #print the result
