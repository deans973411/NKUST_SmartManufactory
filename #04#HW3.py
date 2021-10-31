#HW3
#班級:四模四丙 學號:C107147319 姓名:林鼎鈞
print('HW3')
print('班級:四模四丙 學號:C107147319 姓名:林鼎鈞')

#1-0 輸入班上同學成績，使用串列list
print("1-0 輸入班上同學成績，使用串列list")
print('tip:格式請輸入{成績1}{空格}{成績2}{空格}{成績3}')
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
    IN1 = input('國文/英文/數學>')
    NUM1 = IN1.count(' ')
    if NUM1 == 2:    
        try:
            Chi, Eni, Mai = map(int, IN1.split())
        except:
            print('=輸入成績數量錯誤=')
            continue
        if Chi > 100 or Eni > 100 or Mai > 100:
            print('=輸入成績爆錶=')
            continue
        elif Chi < 0 or Eni < 0 or Mai < 0:
            print('=輸入成績低於0=')
            continue
        else:
            i1 += 1
            Ch.append(Chi)
            En.append(Eni)
            Ma.append(Mai)
            #print(Ch)
            #print(En)
            #print(Ma)
    elif NUM1 == 1 or NUM1 > 2:
        print('==格式錯誤或輸入異常，請重新輸入==')
        continue
    else:
        print('總共輸入了', i1,'筆資料')
        break
print('總共輸出', i1, '筆資料')

#1-a 查詢三科成績皆90分以上人數
print('1-a 查詢三科成績皆90分以上人數')
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
    for i2 in range(0, i1, 1):
        a1 = Ch[i2]
        b1 = En[i2]
        c1 = Ma[i2]
        if a1 >= 90 and b1 >= 90 and c1 >= 90:
            NUM2 += 1
    else:
        print("三科成績達90分共", NUM2, "人")
        break


#1-b 全班國文最高分
print('1-b 全班國文最高分')
try:
    print('全班國文最高分共:', max(Ch), '分')
except ValueError:
    print('No data')
    pass


#1-c 全班數學最高分
print('1-c 全班數學最高分')
try:
    print('全班數學最高分共:', max(Ma), '分')
except ValueError:
    print('No data')
    pass


#1-d 全班英文不及格人數
print('1-d 全班英文不及格人數')
for i3 in range(0, i1, 1):
    c2 = Ma[i3]
    if c2 < 60:
        NUM3 += 1
print('全班英文不及格共:', NUM3, '人')


#1-e 全班國文英文數學的平均分數是多少
print('1-e 全班國文英文數學的平均分數是多少')
for i4 in range(0, i1, 1):
    a3 = int(Ch[i4])
    b3 = int(En[i4])
    c3 = int(Ma[i4])
    VAL1 += (a3 + b3 + c3)
 
print('全班所有成績平均:', (VAL1 / i1 / 3), '分')


#1-f(自行增加) 查詢第幾位同學成績
print('1-f(自行增加) 查詢第幾位同學成績')

print('同學編號:', end='')
for i5 in range(1, i1+1, 1):
    print('{:2}, '.format(i5), end='')
print("\n國文成績", Ch)
print("英文成績", En)
print("數學成績", Ma)
search = int(input('查詢第n筆資料:'))
search = search - 1
a = Ch[search]
b = En[search]
c = Ma[search]
print("\n第", search + 1, "同學成績如下:\n", "國文:", a, "英文:", b, "數學:", c)
