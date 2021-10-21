#班級:四模四丙 學號:C107147319 姓名:林鼎鈞
print("班級:四模四丙 學號:C107147319 姓名:林鼎鈞")

#1-執行1至100迴圈，並顯示21至50間奇數並計算總合
print("1-執行1至100迴圈，並顯示21至50間奇數並計算總合")   

i1 = 0
SUM1 = 0
for i1 in range(1, 100, 1):             #執行1到100迴圈
    if i1 >= 21 and i1 <= 50:           #定義區間
        if i1 % 2 == 1:                 #定義奇數
            print(i1," ", end='')
            SUM1 += i1
print('\n21至50奇數總和為', SUM1)
print('\n')


#2排版整齊的9x9乘法表
print("2-排版整齊的9x9乘法表")

NUM1 = 1
while NUM1 < 10:
    NUM1 += 1
    for y in range(NUM1-1, NUM1):
        for x in range(2, 10):
            print('{}x{}={:2} '.format(x, y, x*y), end='')
    print('\n\n')


#3-輸入10位同學成績，印出全班最高分、最低分與不級格人數
print("3-輸入10位同學成績，印出全班最高分、最低分與不級格人數")
print("***提醒您，設定至多只能輸入10次喔***")

i2 = 1
NUM2 = 0
CLASS_SCORE = list()
CLASS_SCORE.append(input("請輸入成績< 1 >\n"))
while True:
    i2 += 1
    if i2 > 10:
        print("您輸入了10筆成績")
        break
    print("請輸入成績<", i2, ">")
    Std_SCORE = input()
#    Std_SCORE = int(Std_SCORE)
#    if Std_SCORE >= 100 or Std_SCORE <= 0:
#        print("您輸入了異常成績，程式終止(SCORE>100, SCORE<0)")
#        break
    if Std_SCORE == "":
        print("您輸入空白成績，提早終止")
        print("您輸入了", i2-1,"筆資料")
        break
    else:
        CLASS_SCORE.append(Std_SCORE)
CLASS_SCORE = list(map(int, CLASS_SCORE))
for Failed_SCORE in CLASS_SCORE:
    Failed_SCORE = int(Failed_SCORE)
    if Failed_SCORE < 60:
        NUM2 += 1
  
print('您輸入的成績是:', CLASS_SCORE)
print("本班最高分為:", max(CLASS_SCORE), " 本班最低分為:", min(CLASS_SCORE))
print("本班不及格人數為", NUM2)
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
